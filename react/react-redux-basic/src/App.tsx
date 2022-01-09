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
