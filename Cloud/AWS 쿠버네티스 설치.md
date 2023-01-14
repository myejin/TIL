## AWS EKS 환경 구축해보기 - EC2 배포방식 

### 사전 준비사항
- AWS 계정
- 외부 통신이 가능한 서버 또는 VM 
<br>

### AWS Console 에서 EKS Cluster 배포 준비 
- AWS Console 의 IAM(=) 을 통해 사용자 추가 
- AWS CLI 를 사용하기 위해 `AWS 액세스 유형 > 액세스 키 - 프로그래밍 방식 액세스` 선택 
- 사용사 권한 설정 > `AdministratorAccess` 권한 부여
  - EKS 관리를 위한 사용자 권한은 클러스터 관리, 노드, Pod 실행 등 많은 정책으로 세밀하게 구분할 수 있다.
- 사용자 생성 프로시저를 통한 입력값 검토 
- 사용자 생성완료
<br>

### 외부 VM 에서 EKS Cluster 배포 준비 
> Terraform 을 이용한 배포 

- 사전 준비된 외부통신이 가능한 서버에 접속하여, 필수 패키지 설치 및 구성파일 설정
<br>

#### ✔️ Terraform 명령어 설치 
```
...
```

#### ✔️ awscli 설치
```
...
```

#### ✔️ eksctl 명령어 설치 
```
...
```

#### ✔️ 환경변수 파일 다운로드 by Terraform 
```
...
```

#### 🟠 Terraform 스크립트 살펴보기 

eks-cluster.tf
EKS 클러스터에 대한 IAM role 과 SecurityGroup, EKS 클러스터 값 

eks-worker-nodes.tf 
EKS Worker 노드에 대한 IAM role, NodeGroup AutoScaling, NodeGroup 값 

outputs.tf 
파일에 설정된 값을 통해 EKS 배포완료 후 정상적으로 배포되었음을 확인 

providers.tf
EKS 생성할 AWS KEY 값 

variables.tf
EKS 생성할 AWS region, EKS 클러스터 이름 값 

vpc.tf
EKS 가 사용할 Network 환경 구축 (VPC, Subnet, Route) 

<br>

### EKS 배포 

<br>...<br>






### 참고URL
https://tech.osci.kr/2022/11/01/aws-%EC%83%81%EC%97%90-%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-aws-eks/
