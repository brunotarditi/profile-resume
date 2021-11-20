import React from 'react'
import {  ThemeProvider } from '@mui/material/styles';
import theme from './ThemeConfig';
import Main from './components/Main';
function App() {
  return (
    <ThemeProvider theme={theme}>
      <Main />
    </ThemeProvider>
  );
}

export default App;
