import { Toolbar, IconButton, Typography, AppBar } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import Brightness7Icon from '@mui/icons-material/Brightness7';
import Brightness4Icon from '@mui/icons-material/Brightness4';
import { useEffect } from 'react';


const Navbar = (props) => {

    useEffect(() => {
        localStorage.setItem("mode", JSON.stringify(props.theme.palette.mode));
    }, [props.theme.palette.mode]);
    return (
        <AppBar
            position="fixed"
            sx={{
                width: { sm: `calc(100% - ${props.drawerWidth}px)` },
                ml: { sm: `${props.drawerWidth}px` },
            }}
        >
            <Toolbar>
                <IconButton
                    color="inherit"
                    aria-label="open drawer"
                    edge="start"
                    onClick={() => props.handleDrawerOpen()}
                    sx={{ mr: 2, display: { sm: 'none' } }}
                >
                    <MenuIcon />
                </IconButton>
                <Typography variant="h6" noWrap component="div" sx={{ flexGrow: 1 }}>
                    Bruno Tarditi
                </Typography>
                modo {props.theme.palette.mode}
                <IconButton onClick={props.colorMode.toggleColorMode} color="inherit">
                    {props.theme.palette.mode === 'dark' ? <Brightness7Icon /> : <Brightness4Icon />}
                </IconButton>
            </Toolbar>
        </AppBar>
    );
}

export default Navbar
