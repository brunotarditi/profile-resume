import { useState, useMemo, createContext } from 'react'
import { Box } from '@mui/material';
import Sidebar from './components/Sidebar';
import Navbar from './components/Navbar';
import AppRouting from './routes/AppRouting';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { CssBaseline } from '@mui/material';

const ColorModeContext = createContext({ toggleColorMode: () => { } });
function App() {
  const [open, setOpen] = useState(false);
  const [mode, setMode] = useState(() => {
    const storageMode = localStorage.getItem("mode");
    const initialValue = JSON.parse(storageMode);
    return initialValue || "light";
  });
  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };
  const colorMode = useMemo(
    () => ({
      toggleColorMode: () => {
        setMode((prevMode) => (prevMode === 'light' ? 'dark' : 'light'));
      },
    }),
    [],
  );

  const theme = useMemo(
    () =>
      createTheme({
        palette: {
          mode,
        },
      }),
    [mode],
  );
  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <Box sx={{ display: 'flex' }}>
          <CssBaseline />
          <Navbar
            open={open}
            handleDrawerOpen={handleDrawerOpen}
            theme={theme}
            colorMode={colorMode}
          />
          <Sidebar
            open={open}
            handleDrawerClose={handleDrawerClose}
          />
          <AppRouting open={open} />
        </Box >
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
