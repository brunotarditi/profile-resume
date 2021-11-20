import React from 'react'
import { AppBar, Toolbar, IconButton, Typography } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';

const drawerWidth = 240;

const Navbar = (props) => {
    return (
        <AppBar position="fixed" 
        sx={{
            width: { sm: `calc(100% - ${drawerWidth}px)` },
            ml: { sm: `${drawerWidth}px` },
          }}>
            <Toolbar >
                <IconButton 
                edge="start" 
                color="inherit" 
                aria-label="menu" 
                sx={{ mr: 2 }}
                onClick={() => props.handleDrawerOpen()}
                >
                    <MenuIcon />
                </IconButton>
                <Typography 
                    variant="h6" 
                    color="inherit">
                    Bruno Tarditi
                </Typography>
            </Toolbar>
        </AppBar>
    )
}

export default Navbar
