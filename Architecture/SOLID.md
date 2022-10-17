## 📌 SOLID?
> 객체지향 설계의 정수, Robert C. Martin 이 만든 5가지 코딩규칙

- SOLID 원칙은 <b>코드 품질을 높이기 위한</b> 기본학습 단계
- 장점 : 테스트 개선, 기술부채 감소, 새 요구사항에 유연하게 대처 
</br>

### 단일 책임 원칙 (SRP)
> Single Responsibility Principle</br>
> 어떤 클래스를 변경해야 하는 이유는 오직 하나뿐이다. 

- 다른 클래스들이 서로 영향을 미치는 연쇄작용을 줄일 수 있다. (응집도 up, 결합도 down) 
- 책임을 적절하게 분배하여 코드의 가독성 및 유지보수성을 높일 수 있다.
- 코드의 모든 부분은 다른 섹션에서 재사용될 수 있다. 
- 예시
  ```python
  import numpy as np 

  def math_operations(list_):
    print(f"the mean is {np.mean(list_)}")
    print(f"the max is {np.max(list_)}")

  math_operations(list_=[1,2,3,4,5])
  
  ### 개선: math_operations 를 원자함수로 분리 
  
  def get_mean(list_):
    print(f"the mean is {np.mean(list_)}")

  def get_max(list_):
    print(f"the max is {np.max(list_)}")

  def main(list_):
    get_mean(list_)
    get_max(list_)

  main([1, 2, 3, 4, 5]) # 그러나, 이 main 호출기능을 생성하는 것은 SRP의 완전한 이행이 아니다. 다음 원칙을 보면..
  ```
</br>

### 개방-폐쇄 원칙 (OCP)
> Open Closed Principle</br>
> 엔티티(클래스, 모듈, 함수 등) 확장에 대해서는 열려있어야 하지만, 수정을 위해 닫혀있어야 한다. 

- 새 기능을 수용하기 위해, 코드를 추가하지만 기존 코드의 다른 부분을 수정할 필요가 없다.
- 예시
  ```python  
  ### 개선: 새 기능 추가 또는 기존 기능 수정/삭제 시, main 수정은 없도록 한다. 
  
  from abc import ABC, abstractmethod

  class Operations(ABC):
    @abstractmethod
    def operation():
      pass 

  class Mean(Operations):
    def operation(list_):
      print(f"The mean is {np.mean(list_)}")

  class Max(Operations):
    def operation(list_):
      print(f"The max is {np.max(list_)}")

  class Median(Operations):
    def operation(list_):
      pass # 새 기능 추가 

  class Main:
    @abstractmethod 
    def get_operations(list_):
      for operation in Operations.__subclass__():
        operation.operation(list_)

  if __name__ == "__main__":
    Main.get_operations([1,2,3,4,5])
  ```
  - 예시2
    - 
</br>

### 리스코프 치환 원리 (LSP)
> Listov Substitution Principle</br> 
> 서브 타입은 언제나 자신의 기반 타입으로 교체할 수 있어야 한다. 

- 자식클래스가 부모클래스의 함수를 오버라이딩하면, 두 함수는 동일한 입력일 때 동일한 유형의 결과를 내고 대체가능해야 한다.
- 상속은 하되 오버라이딩 하지 않으면, LSP 를 지킬 수 있다. 하지만 무조건적인 방법은 아니다. 
- 오버라이딩이 필요하다면, <b>자식클래스가 부모클래스의 의미를 해치지 않게 기존 역할을 충실히 수행</b>하고, 기능의 추가만 신중하게 고민 후 수행한다.
</br>

### 인터페이스 분리 원칙 (ISP)
> Interface Segregation Principle</br>
> 많은 클라이언트 별 인터페이스가 하나의 범용 인터페이스보다 낫다.

- 클라이언트는 자신이 사용하지 않는 메소드에 의존성을 가지면 안 된다. 인터페이스를 작은 단위로 분리하여 꼭 필요한 인터페이스만 상속받자 
- SRP 가 클래스의 단일책임을 강조했다면, ISP 는 인터페이스의 단일책임을 강조한다. 
  - 같은 문제를 다르게 해결할 수 있다.
  - SRP 는 하나의 역할만 하도록 다수의 클래스를 분리한다면, ISP 는 각 역할에 맞게 인터페이스로 분리한다.
</br>

### 의존성 역정 원칙 (DIP)
> Dependency Inversion Principle</br>
> 고수준 모듈은 저수준 모듈에 종속되면 안 된다. 모두 다른 추상화된 것에 의존해야 한다.
> 자주 변경되는 클래스에 의존하면 안 된다.

- 예시
  ```javascript
  // bad case 

  interface ChildProps {
    value: string;
    setValue: (value: string) => void;
  }
  const Child = ({ value, setValue }: ChildProps) => {
      if (value !== 'apple') {
        return setValue('banana');
      } else {
        return setValue('cake');
      }
  };

  const Parent = () => {
    const [value, setValue] = useState(''); 
    return <Child value={value} setValue={setValue} />; // 부모자식 간 의존성 존재 
  };
  
  // 개선: doAction 으로 변경해 의존성 제거

  interface ChildProps {
    value: string;
    doAction?: (value: string) => void;
  }
  const Child = ({ value, doAction }: ChildProps) => {
      if (value !== 'apple') {
        return doAction?.('banana');
      } else {
        return doAction?.('cake');
      }
  };
  
  const Parent1 = () => {
    const [value, setValue] = useState('');
    return <Child value={value} doAction={v => setValue(v)} />; // setValue 를 바로 넘겨주지 않는다. 
  };  
  const Parent2 = () => {
    const value = 'daddy'; // setValue 필요없음
    return <Child value={value} doAction={v => console.log(v)} />; // 다른 로직을 주입해도 동작
  };
</br>

### 참고글
- https://brunch.co.kr/@springboot/30
- https://towardsdatascience.com/solid-coding-in-python-1281392a6a94
- https://jaeyeong951.medium.com/%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5-5%EC%9B%90%EC%B9%99-solid-ac7d4d660f4d
- https://devlog-wjdrbs96.tistory.com/m/380

