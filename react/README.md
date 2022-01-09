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

<br>

> store (1) react-redux X / props O  

- `index.tsx`

```tsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {createStore, Store} from 'redux';

// 1) action 타입 
const ADD_AGE = 'ADD_AGE';

// 2) action creator
export function addAge() {
  return {
    type: ADD_AGE
  };
}

// 3) 리듀서 (평범한 함수)
function ageApp(state: {age: number;} = {age: 27}, action: {type: string}) {
  if (action.type === ADD_AGE) {
    return {
      age: state.age + 1
    };
  }
  return state;
}

// 4) store
const store: Store<{age: number;}> = createStore(ageApp);

// store에서 뭔가 변화가 일어나면 다시 렌더링 하는 것
store.subscribe(render);

function render() {
  ReactDOM.render(
    <React.StrictMode>
      <App store={store} />
    </React.StrictMode>,
    document.getElementById('root')
  );
}

render();
```

- `App.tsx`

```tsx
import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Store} from 'redux';
import {addAge} from './index';

class App extends React.Component<{store: Store<{age: number;}>}, {}> {
  render() {
    const store = this.props.store;
    const state = store.getState();

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {state.age} 
            <button onClick={() => {
              store.dispatch(addAge()); 
            }}>한해가 지났다.</button>
          </p>
        </header>
      </div>
    );
  }
}

export default App;
```

<br>

> store (2) react-redux X / props O  

- `index.tsx`

```tsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {createStore, Store} from 'redux';

// 1) action 타입 
const ADD_AGE = 'ADD_AGE';

// 2) action creator
export function addAge() {
  return {
    type: ADD_AGE
  };
}

// 3) 리듀서 (평범한 함수)
function ageApp(state: {age: number;} = {age: 27}, action: {type: string}) {
  if (action.type === ADD_AGE) {
    return {
      age: state.age + 1
    };
  }
  return state;
}

// 4) store
const store: Store<{age: number;}> = createStore(ageApp);

ReactDOM.render(
  <React.StrictMode>
    <App store={store} />
  </React.StrictMode>,
  document.getElementById('root')
);
```

- `App.tsx`

```tsx
import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Store, Unsubscribe} from 'redux';
import {addAge} from './index';

class App extends React.Component<{store: Store<{age: number;}>}, {}> {
  private _unsubscribe: Unsubscribe;
  componentDidMount() {
    const store = this.props.store;
    this._unsubscribe = store.subscribe(() => {
      this.forceUpdate();
    });
  }
  componentWillUnmount() {
    this._unsubscribe();
  }

  render() {
    const store = this.props.store;
    const state = store.getState();
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {state.age} 
            <button onClick={() => {
              store.dispatch(addAge()); 
            }}>한해가 지났다.</button>
          </p>
        </header>
      </div>
    );
  }
}

export default App;
```

<br>

> store (2) react-redux X / props X / context O  

- `index.tsx`

```tsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as PropTypes from 'prop-types';
import {createStore, Store} from 'redux';

// 1) action 타입 
const ADD_AGE = 'ADD_AGE';

// 2) action creator
export function addAge() {
  return {
    type: ADD_AGE
  };
}

// 3) 리듀서 (평범한 함수)
function ageApp(state: {age: number;} = {age: 27}, action: {type: string}) {
  if (action.type === ADD_AGE) {
    return {
      age: state.age + 1
    };
  }
  return state;
}

// 4) store
const store: Store<{age: number;}> = createStore(ageApp);

// 5) provider 생성
class Provider extends React.Component<{store: Store<{age: number;}>}, {}> {
  static childContextTypes = {
    store: PropTypes.object 
  };
  getChildContext() {
    return {
      store: this.props.store
    };
  }
  render() {
    return this.props.children as JSX.Element;
  }
}

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);
```

- `App.tsx`

```tsx
import React from 'react';
import logo from './logo.svg';
import './App.css';
import * as PropTypes from 'prop-types';
import {Unsubscribe} from 'redux';
import {addAge} from './index';

class App extends React.Component<{}, {}> {
  static contextTypes = {
    store: PropTypes.object
  }; 
  private _unsubscribe: Unsubscribe;
  componentDidMount() {
    const store = this.context.store;
    this._unsubscribe = store.subscribe(() => {
      this.forceUpdate();
    });
  }
  componentWillUnmount() {
    this._unsubscribe();
  }

  render() {
    const store = this.context.store;
    const state = store.getState();
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {state.age} 
            <button onClick={() => {
              store.dispatch(addAge()); 
            }}>한해가 지났다.</button>
          </p>
        </header>
      </div>
    );
  }
}

export default App;
```

<br>

> react-redux

- provider 컴포넌트를 제공하는 모듈
- `index.tsx`

```tsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {createStore, Store} from 'redux';
import {Provider} from 'react-redux';

// 1) action 타입 
const ADD_AGE = 'ADD_AGE';

// 2) action creator
export function addAge() {
  return {
    type: ADD_AGE
  };
}

// 3) 리듀서 (평범한 함수)
function ageApp(state: {age: number;} = {age: 27}, action: {type: string}) {
  if (action.type === ADD_AGE) {
    return {
      age: state.age + 1
    };
  }
  return state;
}

// 4) store
const store: Store<{age: number;}> = createStore(ageApp);

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);
```

- `App.tsx`

```tsx
import logo from './logo.svg';
import './App.css';
import {addAge} from './index';
import {connect} from 'react-redux';

interface AppProps {
  age: number;
  onAddClick(): void;
}

// stateless 함수로 변경 
const App = (props: AppProps) => {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          {props.age} 
          <button onClick={() => props.onAddClick()}>한해가 지났다.</button>
        </p>
      </header>
    </div>
  );
}

const mapStateToProps = (state: {age: number;}) => {
  // App 컴포넌트에서만 쓰는 state 데이터 = 컨테이너
  return {
    age: state.age,
  };
};

const mapDispatchToProps = (dispatch: Function) => {
  return {
    onAddClick: () => {
      dispatch(addAge());
    }
  };
}

// connect 함수를 통해 컨테이너를 만들어준다. 
const AppContainer = connect(
  mapStateToProps,
  mapDispatchToProps 
)(App);

export default AppContainer;
```

