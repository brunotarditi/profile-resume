import React from 'react'
import { Box } from '@mui/material';
import Sidebar from './Sidebar';
import Navbar from './Navbar';
const Experience = () => {
    const [open, setOpen] = React.useState(false);
    const handleDrawerOpen = () => {
        setOpen(true);
    };

    const handleDrawerClose = () => {
        setOpen(false);
    };
    return (
        <Box sx={{ display: 'flex' }}>
            <Navbar
                open={open}
                handleDrawerOpen={handleDrawerOpen} />
            <Sidebar
                open={open}
                handleDrawerClose={handleDrawerClose}
            />
            <h1>
                Mi experiencia
            </h1>
        </Box>
    )
}

export default Experience
