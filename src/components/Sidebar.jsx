import React from 'react'
import { Drawer, IconButton, Divider } from '@mui/material';
import ItemList from './ItemList';
import { styled, useTheme } from '@mui/styles';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';

const drawerWidth = 240;

const DrawerHeader = styled('div')(({ theme }) => ({
    display: 'flex',
    alignItems: 'center',
    padding: theme.spacing(0, 1),
    ...theme.mixins.toolbar,
    justifyContent: 'flex-end',
}));

const Sidebar = (props) => {

    const theme = useTheme();
    return (
        <div>
            <Drawer
                sx={{
                    width: drawerWidth,
                    flexShrink: 0,
                    '& .MuiDrawer-paper': {
                        width: drawerWidth,
                        boxSizing: 'border-box',
                    },
                }}
                variant="persistent"
                anchor="left"
                open={props.open}
            >
                <DrawerHeader>
                    <IconButton  onClick={() => props.handleDrawerClose()}>
                        {theme.direction === 'ltr' ? <ChevronLeftIcon /> : <ChevronRightIcon />}
                    </IconButton>
                </DrawerHeader>
                <Divider />
                <ItemList />
            </Drawer>

        </div>
    );
}

export default Sidebar
