import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages/Home';
import Classes from './pages/Classes';
import Progress from './pages/Progress';

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/Classes' component={Classes} />
          <Route path='/Progress' component={Progress} />
        </Switch>
      </Router>
    </>
  );
}

export default App;
