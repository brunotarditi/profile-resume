import React from 'react'
import { Box, Hidden } from '@mui/material';
import Navbar from './Navbar';
import Sidebar from './Sidebar';
import Content from './Content';

const Main = () => {
    const [openDrawer, setOpen] = React.useState(false);

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };
    return (
        <Box sx={{ display: 'flex' }}>
            <Navbar handleDrawerOpen={handleDrawerOpen}/>
            <Hidden xsDown>
                <Sidebar
                    variant="permanent"
                    open={true}
                />
            </Hidden>
            <Hidden smUp>
                <Sidebar
                    variant="temporary"
                    open={openDrawer}
                    onClose={handleDrawerClose}
                />
            </Hidden>
            <Content />
        </Box >
    )
}

export default Main
