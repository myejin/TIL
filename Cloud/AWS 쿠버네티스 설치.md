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
  <img width="600" alt="image" src="https://user-images.githubusercontent.com/42771578/212703436-cc3335b7-1b4c-4354-a1ee-a3758ab5b1c6.png">


#### ✔️ eksctl 명령어 설치 
```bash
~$ curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
~$ sudo mv /tmp/eksctl /usr/local/bin
```
<img width="300" alt="image" src="https://user-images.githubusercontent.com/42771578/212704050-16272754-22be-4228-a203-825375959236.png">

#### ✔️ 환경변수 파일 다운로드 by Terraform 
```bash
~$ git clone https://github.com/terraform-providers/terraform-provider-aws.git
~$ cp -rp ~/eks-getting-started ~/aws-eks 

~/aws-eks$ ls
README.md       eks-worker-nodes.tf  providers.tf  vpc.tf
eks-cluster.tf  outputs.tf           variables.tf  workstation-external-ip.tf
```

<br>

### EKS 배포 
```
~/aws-eks$ terraform init
...
Terraform has been successfully initialized!
...

ubuntu@ip-172-31-47-132:~/aws-eks$ terraform --version
Terraform v1.3.7
on linux_amd64
+ provider registry.terraform.io/hashicorp/aws v4.51.0
+ provider registry.terraform.io/hashicorp/http v3.2.1

ubuntu@ip-172-31-47-132:~/aws-eks$ terraform apply
Error: configuring Terraform AWS Provider: no valid credential sources for Terraform AWS Provider found.

```
<br>

### EKS Cluster 배포 확인 
- kubectl 명령어 설치 
- EKS kubeconfig 파일


EKS 에서는 마스터노드(=Control Plane)을 AWS 자체에서 관리하기 때문에,
kubectl get nodes > 워커노드만 확인할 수 있다. 
AWS에서 EC2가 하나 생성된 것을 볼 수 있다. 
<br> 

### AWS ALB Ingress 배포 준비 

EKS Ingress 를 생성할 때 애플리케이션 트래픽을 로드밸런싱하는 ALB 가 프로비저닝 된다.

ALB 사용을 위해 ALB Ingress Controller 를 구성하자! 

IAM OIDC 자격증명 공급자 생성

EKS 의 Service Account 에 IAM Role 을 적용하기 위해 IAM OIDC 자격증명 공급자를 생성한다.

IAM Role 을 만들어준다. Role 이름은 AWSLoadBalancerControllerIAMPolicy 이며,
이 Role 은 AWS 로드밸런서 컨트롤러가 사용자를 대신하여 AWS API 를 호출할 수 있도록 허용한다. 

Arn 값은 아래 Service Account 만드는 부분에서 사용해야하니 메모해둔다.

위에서 생성한 IAM Role 을 기반으로 Service Account 를 생성해주고, 
EKS 클러스터 내의 TLS 인증서를 자동으로 프로비저닝 하기위해 Cert-Manager 배포한다. 


VPC Subnet Tag 
ALB 리소스가 생성될 때, AWS 로드밸런서 컨트롤러가 서브넷을 자동으로 검색할 수 있도록
Amazon EKS 클러스터에서 Amazon VPC 서브넷에 태깅한다. 

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
