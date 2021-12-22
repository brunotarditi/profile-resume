import { useState, useMemo, createContext } from 'react'
import { Box, Toolbar } from '@mui/material';
import Sidebar from './components/Sidebar';
import Navbar from './components/Navbar';
import AppRouting from './routes/AppRouting';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { CssBaseline } from '@mui/material';

const ColorModeContext = createContext({ toggleColorMode: () => { } });
const drawerWidth = 240;

function App(props) {
  const { window } = props;
  const [open, setOpen] = useState(false);

  const [mode, setMode] = useState(() => {
    const storageMode = localStorage.getItem("mode");
    const initialValue = JSON.parse(storageMode);
    return initialValue || "light";
  });

  const handleDrawerOpen = () => {
    setOpen(!open);
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

  const container = window !== undefined ? () => window().document.body : undefined;
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
            drawerWidth={drawerWidth}
          />
          <Sidebar
            open={open}
            onClose={handleDrawerOpen}
            container={container}
            drawerWidth={drawerWidth}
          />
          <Box
            component="main"
            sx={{ flexGrow: 1, p: 3, width: { sm: `calc(100% - ${drawerWidth}px)` } }}
          >
            <Toolbar />
            <AppRouting open={open} />
          </Box >
        </Box >
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
