## AWS EKS 환경 구축해보기 - EC2 배포방식 

### 사전 준비사항
- AWS 계정
- 외부 통신용 서버 또는 VM
<br>

### AWS Console 에서 EKS Cluster 배포 준비 
- IAM(=Identity and Access Management) 사용자 추가
- AWS CLI 사용을 위해, `AWS 액세스 유형` > `액세스 키 - 프로그래밍 방식 액세스` 선택
- `AdministratorAccess` 권한 부여<br>
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

# 복사한 파일 커스텀 수정 
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
# kubectl 설치 
~/aws-eks$ curl -o kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.23.7/2022-06-29/bin/linux/amd64/kubectl
~/aws-eks$ chmod +x ./kubectl
~/aws-eks$ mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
~/aws-eks$ echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc

~/aws-eks$ kubectl version --short --client
Client Version: v1.23.7-eks-4721010

~/aws-eks$ aws configure
AWS Access Key ID: ..
AWS Secret Access Key: .. 
Default region name: .. 
Default output format: ..

~/aws-eks$ aws eks update-kubeconfig --name terraform-eks-hj
Added new context..

# AWS가 관리하는 Master 노드 제외, Worker 노드 확인 
~/aws-eks$ kubectl get nodes
...
```
<img width="650" alt="image" src="https://user-images.githubusercontent.com/42771578/221858482-d393ce3b-8571-4d62-b6fb-c2ea19567ac7.png">

<br> 

### AWS ALB Ingress 배포 준비 

#### ✔️ ALB Ingress Controller 구성 (for ALB 사용) 
```bash 
# IAM OIDC 자격증명 공급자 생성
~$ eksctl utils associate-iam-oidc-provider --region=ap-northeast-2 --cluster=terraform-eks-hj --approve 
~$ curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json 

# IAM Role "AWSLoadBalancerControllerIamPolicy" 생성 
# AWS 로드밸런서 컨트롤러가 사용자를 대신하여 AWS API 를 호출하도록 허용한다. 
~$ aws iam create-policy --policy-name AWSLoadBalancerControllerIAMPolicy --policy-document file://iam-policy.json
{
    "Policy": {
        "PolicyName": "AWSLoadBalancerControllerIAMPolicy",
        ...
    }
}

# IAM Role 기반 Service Account 생성
~$ eksctl create iamserviceaccount --cluster=terraform-eks-hj --namespace=kube-system --name=aws-load-balancer-controller --attach-policy-arn=arn:aws:iam::{~}:policy/AWSLoadBalancerControllerIAMPolicy --override-existing-serviceaccounts --approve

# Cert-Manager 배포 (for EKS 클러스터 내 TLS 인증서 프로비저닝) 
~$ kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v1.9.1/cert-manager.yaml
```

#### ✔️ VPC SubNet Tag
> 컨트롤러가 서브넷을 자동으로 검색할 수 있도록 VPC 서브넷에 태깅
<img width="450" alt="image" src="https://user-images.githubusercontent.com/42771578/221859392-c8173923-678e-4ed2-84fa-95f5405d913a.png">

<br>

> Ingress 생성 시 권한오류를 방지하기 위해, IAM EKS 클러스터 및 노드의 role 에 Policy 추가
<img width="500" alt="image" src="https://user-images.githubusercontent.com/42771578/221860491-79fbb163-f311-451d-8ced-34ff3ae370c7.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/42771578/221860654-aadd9821-aa1d-49e5-809e-b06de7f73c68.png">

<br>

### AWS ALB Ingress Controller 배포 

```bash 
~$ curl -Lo ingress-controller.yaml https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/download/v2.4.4/v2_4_4_full.yaml
~$ cp ingress-controller.yaml ingress-controller.bak
~$ diff -u ingress-controller.bak ingress-controller.yaml
~$ kubectl apply -f ingress-controller.yaml
```

### AWS ALB Ingress Controller 배포 확인 

```bash
~$ kubectl get all -n kube-system
```
<img width="700" alt="image" src="https://user-images.githubusercontent.com/42771578/221861992-870074e9-2bdd-461c-b771-4fd8c96be73e.png">

```bash
# 웹 서버 올려서 ingress 테스트 
~$ kubectl apply -f flask-deployment.yaml 
~$ kubectl apply -f flask-ingress.yaml
```

<br>

### AWS EKS Cluster 삭제 

```bash
~$ terraform destroy
...
```

### 참고URL
https://tech.osci.kr/2022/11/01/aws-%EC%83%81%EC%97%90-%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-aws-eks/
