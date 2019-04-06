import React,{Component} from 'react';
import ReactDOM from 'react-dom';
import App,{ErrorBoundary} from './components/App';

ReactDOM.render(<ErrorBoundary>
    <App />
</ErrorBoundary>, document.querySelector('#app'));