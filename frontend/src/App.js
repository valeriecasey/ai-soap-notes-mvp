import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import FileUpload from './components/FileUpload';
import NoteDisplay from './components/NoteDisplay';

function App() {
  return (
    <Router>
      <div className="App">
        <h1>AI-Powered SOAP Notes</h1>
        <Switch>
          <Route path="/" exact component={FileUpload} />
          <Route path="/notes" component={NoteDisplay} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;