> 프로젝트 생성 및 실행 

```
$ npm i create-react-app -g 
$ create-react-app react-basic --template typescript
$ cd react-basic/
$ npm start
```

<br>



> props와 state 활용, Lifecycle 이해 

- `App.tsx`

```tsx
import React from 'react';

interface AppProps {
  name: string;
  company?: string; 
}

interface AppState {
  age: number;
}

class App extends React.Component<AppProps, AppState> {
  static defaultProps = {
    company: 'Prelancer'
  };
  constructor(props: AppProps) {
    console.log('constructor');
    super(props); 
    this.state = { // 초기세팅, 이후에는 readonly 이기 때문에 변경불가 
      age: 27
    };
    this._rollback = this._rollback.bind(this)
  }

  // LifeCycle 
  componentDidUpdate() {
    console.log('component Did Update');
    
  }
  componentDidMount() {
    console.log('component Did Mount');
    setInterval(() => {
      this.setState({
        age: this.state.age + 1 
      });
    }, 2000);
  }

  componentWillUnmount() {
    console.log('component Will Unmount');
    // 메모리 누수를 막기위해 사용, 여기서 할당해제 해야함
  }

  shouldComponentUpdate(nextProps: AppProps, nextState: AppState): boolean {
    // props 또는 state 가 변경되면 호출된다. 
    console.log(`should Component Update: ${JSON.stringify(nextProps)}, ${JSON.stringify(nextState)}`);
    return true; // false라면 렌더링되지 않는다. (componentDidUpdate가 호출되지 않는다.)
  }

  render(): React.ReactNode {
    return (
      <div className="App">
        <h2>{this.props.name}, {this.props.company}, {this.state.age}</h2>
        <button onClick={this._rollback}>젊어지자</button>
        <StatelessComponent name="Daphne" />
      </div>
    );
  }

  private _rollback(): void {
    this.setState({ // 함수에 this를 바인딩한 후 사용할 수 있다. 
      age: 27
    });
  }
}

const StatelessComponent = ({name='', company='Home'}) => {
  // props 를 풀어서 쓴 것 
  return (
    <h2>[StatelessComponent] {name}, {company}</h2>
  );
}

export default App;
```

<br>

> react-router 활용

```
$ npm i react-router-dom @types/react-router-dom
```

<br>

> 예제 (v6)

- `App.tsx`

```tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useParams, useNavigate, useLocation} from 'react-router-dom';

const Post = () => {
  const { postId } = useParams<{postId: string}>();
  const { search } = useLocation();  // 쿼리스트링
  const navigate = useNavigate();  // usehistory >> useNavigate 
  
  function goNextPost(): void {
    const nextPostIt: number = Number(postId) + 1; 
    navigate(`/posts/${nextPostIt}`);
  }

  return (
    <div>
      <h3>Post {postId}</h3>
      <button onClick={goNextPost}>next post</button>
      <p>쿼리스트링: { new URLSearchParams(search).get('query') }</p>
    </div>
  );
};

const NotFound = () => {
  return (
    <h3>Not Found</h3>
  );
};

class App extends React.Component<{}, {}> {
  render(): React.ReactNode {
    return (
      <Router>
        <div className="App">
          <div className="App-header">
            <h2>Welcome to React</h2>
          </div>
          <nav>
            <ul>
              <li><Link to="/" >Home</Link></li>
              <li><Link to="/intro" >소개</Link></li>
              <li><Link to="/posts/1" >포스트</Link></li>
            </ul>
          </nav>
          <Routes>  {/* Switch가 Routes 로 변경되었다. */}
            <Route path="/" element={<h3>Home</h3>} />
            <Route path="/intro" element={<h3>소개</h3>} />
            <Route path="/posts/:postId" element={<Post />} />
            <Route path="/*" element={<NotFound />} />
          </Routes>
        </div>
      </Router>
    );
  }
}

export default App;
```

