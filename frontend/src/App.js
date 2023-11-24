import './App.css';
import axios from 'axios';

import { useState, createContext, useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';

import Layout from './pages/Layout';
import LoginPage from './pages/LoginPage';
import HomePage from './pages/HomePage';

export const UserContext = createContext();

function App() {

  const [user, setUser] = useState(false);

  const userValue = { user, setUser }

  return (
    <UserContext.Provider value={userValue}>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={user ? <HomePage /> : <LoginPage />} />
        </Route>
      </Routes>
    </UserContext.Provider>
    
  );
}

export default App;
