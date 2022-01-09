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
