import { Drawer, Box, Divider, Toolbar } from '@mui/material';
import ItemList from './ItemList';

const Sidebar = (props) => {
    const drawer = (
        <div>
            <Toolbar />
            <Divider />
            <ItemList />
        </div>
    );
    return (
        <Box
            component="nav"
            sx={{ width: { sm: props.drawerWidth }, flexShrink: { sm: 0 } }}
            aria-label="mailbox folders"
        >
            <Drawer
                container={props.container}
                variant="temporary"
                open={props.open}
                onClose={props.onClose}
                ModalProps={{
                    keepMounted: true,
                }}
                sx={{
                    display: { xs: 'block', sm: 'none' },
                    '& .MuiDrawer-paper': { boxSizing: 'border-box', width: props.drawerWidth },
                }}
            >
                {drawer}
            </Drawer>
            <Drawer
                variant="permanent"
                sx={{
                    display: { xs: 'none', sm: 'block' },
                    '& .MuiDrawer-paper': { boxSizing: 'border-box', width: props.drawerWidth },
                }}
                open={props.open}
            >
                {drawer}
            </Drawer>
        </Box>
    );
}

export default Sidebar
