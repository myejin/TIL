## AWS EKS 환경 구축해보기 - EC2 배포방식 

### 사전 준비사항
- AWS 계정
- 외부 통신용 서버 또는 VM
<br>

### AWS Console 에서 EKS Cluster 배포 준비 
- `AWS Console` > `IAM(=Identity and Access Management)` > `사용자` > `사용자 추가` 진입
- AWS CLI 사용을 위해, `AWS 액세스 유형` > `액세스 키 - 프로그래밍 방식 액세스` 선택
- `권한 설정` > `AdministratorAccess` 권한 부여<br>
  (참고 - 클러스터 관리, 노드, Pod 실행 등 정책을 세밀하게 구분하여 EKS 를 관리할 수 있다.)
<br>
  <img width="450" alt="image" src="https://user-images.githubusercontent.com/42771578/212697442-88db2160-3507-4d05-9677-0e7cb9759a8e.png">

<br>

### 외부 서버(또는 VM)에서 EKS Cluster 배포 준비 
> Terraform 을 이용한 배포 

#### ✔️ Terraform 명령어 설치 
```bash
# 참고 : https://www.hashicorp.com/official-packaging-guide
~$ apt-get update && sudo apt-get install -y gnupg software-properties-common
~$ wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee > /usr/share/keyrings/hashicorp-archive-keyring.gpg
~$ gpg --no-default-keyring --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg --fingerprint
~$ echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee > /etc/apt/sources.list.d/hashicorp.list
~$ apt update
~$ apt-get install terraform
```
  <img width="400" alt="image" src="https://user-images.githubusercontent.com/42771578/212701940-f9c97828-6a6d-4491-860a-c1119f7de273.png">


#### ✔️ awscli 설치
```bash
~$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
~$ unzip awscliv2.zip 
~$ sudo ./aws/install
```
  <img width="580" alt="image" src="https://user-images.githubusercontent.com/42771578/212703436-cc3335b7-1b4c-4354-a1ee-a3758ab5b1c6.png">


#### ✔️ eksctl 명령어 설치 
```bash
~$ curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
~$ sudo mv /tmp/eksctl /usr/local/bin
```
<img width="410" alt="image" src="https://user-images.githubusercontent.com/42771578/212704050-16272754-22be-4228-a203-825375959236.png">

#### ✔️ 환경변수 파일 다운로드 및 설정 by Terraform 
```bash
~$ git clone https://github.com/terraform-providers/terraform-provider-aws.git
~$ cp -rp ~/eks-getting-started ~/aws-eks 

# 복사한 파일 수정 
~/aws-eks$ ls
README.md       eks-worker-nodes.tf  providers.tf  vpc.tf
eks-cluster.tf  outputs.tf           variables.tf  workstation-external-ip.tf
```

<br>

### EKS 배포 
```bash
~/aws-eks$ terraform init
...
Terraform has been successfully initialized!
...

~/aws-eks$ terraform --version
Terraform v1.3.7
on linux_amd64
+ provider registry.terraform.io/hashicorp/aws v4.51.0
+ provider registry.terraform.io/hashicorp/http v3.2.1

~/aws-eks$ terraform apply
...
aws_eks_cluster.hj: Creation complete after 8m25s [id=terraform-eks-hj]
...
aws_eks_node_group.hj: Creation complete after 2m51s [id=terraform-eks-hj:hj]
Apply complete! Resources: 18 added, 0 changed, 0 destroyed.

Outputs:
...
EOT
```
<br>

### EKS Cluster 배포 확인

```bash 
# kebectl 설치 
~/aws-eks$ curl -o kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.23.7/2022-06-29/bin/linux/amd64/kubectl
~/aws-eks$ chmod +x ./kubectl
~/aws-eks$ mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
~/aws-eks$ echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc

~/aws-eks$ kubectl version --short --client
Client Version: v1.23.7-eks-4721010

~/aws-eks$ aws configure
...

~/aws-eks$ aws eks update-kubeconfig --name terraform-eks-hj
Added new context arn:aws:eks:us-west-2:093754923275:cluster/terraform-eks-hj to /home/ubuntu/.kube/config

# AWS가 관리하는 Master 노드 제외, Worker 노드 확인 
~/aws-eks$ kubectl get nodes
NAME                                      STATUS   ROLES    AGE   VERSION
ip-10-0-0-96.us-west-2.compute.internal   Ready    <none>   19m   v1.23.13-eks-fb459a0
```
 
<br> 

### AWS ALB Ingress 배포 준비 

#### ✔️ ALB Ingress Controller 구성 (for ALB 사용) 
```bash 
# IAM OIDC 자격증명 공급자 생성
~$ eksctl utils associate-iam-oidc-provider --region=us-west-2 --cluster=terraform-eks-hj --approve 
~$ curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json 

# IAM Role "AWSLoadBalancerControllerIamPolicy" 생성 
# AWS 로드밸런서 컨트롤러가 사용자를 대신하여 AWS API 를 호출하도록 허용한다. 
~$ aws iam create-policy --policy-name AWSLoadBalancerControllerIAMPolicy --policy-document file://iam-policy.json
{
    "Policy": {
        "PolicyName": "AWSLoadBalancerControllerIAMPolicy",
        "PolicyId": "{~}",
        "Arn": "arn:aws:iam::{~}:policy/AWSLoadBalancerControllerIAMPolicy",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 0,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "CreateDate": "2023-02-06T12:16:29+00:00",
        "UpdateDate": "2023-02-06T12:16:29+00:00"
    }
}

# IAM Role 기반 Service Account 생성
~$ eksctl create iamserviceaccount --cluster=terraform-eks-hj --namespace=kube-system --name=aws-load-balancer-controller --attach-policy-arn=arn:aws:iam::{~}:policy/AWSLoadBalancerControllerIAMPolicy --override-existing-serviceaccounts --approve

# Cert-Manager 배포 (for EKS 클러스터 내 TLS 인증서 프로비저닝) 
~$ kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v1.9.1/cert-manager.yaml

```

#### ✔️ VPC SubNet Tag
> 컨트롤러가 서브넷을 자동으로 검색할 수 있도록 VPC 서브넷에 태깅 



EKS 클러스터에서 Ingress 를 생성할 때 권한오류를 방지하기 위해 IAM 의 EKS 클러스터 역할과
EKS 노드역할에 AdministratorAccess Policy 를 추가한다. 

<br>

### AWS ALB Ingress Controller 배포 

ALB Ingress Controller 를 배포하자.
yaml 파일 내의 클러스터 이름 수정 후 배포한다. 


### AWS ALB Ingress Controller 배포 확인 


배포한 Ingress 를 사용하기 위해 WEB 서비스 하나 배포해보자.
Python Flask 를 통해 Docker Image 를 먼저 Build 하자.


Ingress 정책이 정상적으로 만들어졌고, AWS Console 에서도 내용을 확인할 수 있다. 

서비스가 정상적으로 호출된다! 

<br>

### AWS EKS Cluster 삭제 


Fargate 를 이용하면, Pod 당 1개의 EC2가 배포된다.
사용하는 리소스만큼의 비용에 대해서만 지불하면 된다. 
인프라적 측면의 관리가 별도로 필요하지 않다.

하지만, Fargate 는 DaemonSet 방식의 배포가 불가능하다. 
Privileged Container 지원하지 않는다. 
GPU Pods 사용에 제한적일 수 있다. 
리소스가 제한적이기 때문에 AWS 에서 지원하는 구성을 사용해야한다.
인프라의 관리 없이 어플리케이션에 집중하기 위해선 Fargate 가 더 나은 선택일 수도 있다. 










### 참고URL
https://tech.osci.kr/2022/11/01/aws-%EC%83%81%EC%97%90-%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-aws-eks/
