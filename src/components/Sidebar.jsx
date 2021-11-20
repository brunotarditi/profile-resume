import React from 'react'
import { Drawer, Box } from '@mui/material';
import ItemList from './ItemList';
const drawerWidth = 240;

const Sidebar = (props) => {
    const { window } = props;
    const container = window !== undefined ? () => window().document.body : undefined;
    return (
        <Box
            component="nav"
            sx={{ width: { sm: drawerWidth }, flexShrink: { sm: 0 } }}
            aria-label="mailbox folders"
        >
            <Drawer
                container={container}
                variant="temporary"
                open={props.ope}
                onClose={props.onClose ? props.onClose : null}
                ModalProps={{
                    keepMounted: true,
                }}
                sx={{
                    display: { xs: 'block', sm: 'none' },
                    '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
                }}
            >
                <ItemList />
            </Drawer>
            <Drawer
                variant={props.variant}
                sx={{
                    display: { xs: 'none', sm: 'block' },
                    '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
                }}
                open={props.open}
            >
                <ItemList />
            </Drawer>
        </Box>
    )
}

export default Sidebar
