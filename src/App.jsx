import React from 'react'
import {  ThemeProvider } from '@mui/material/styles';
import { CssBaseline } from '@mui/material';
import theme from './ThemeConfig';
import AppRouting from './components/AppRouting';
function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AppRouting />
    </ThemeProvider>
  );
}

export default App;
