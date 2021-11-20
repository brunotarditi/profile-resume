import React from 'react'
import {  List, ListItem, ListItemIcon, ListItemButton, ListItemText, Toolbar, Divider } from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import WorkIcon from '@mui/icons-material/Work';
const ItemList = () => {
    return (
        <div>
            <Toolbar />
            <Divider />
            <List component='nav'>
                <ListItem>
                    <ListItemButton>
                        <ListItemIcon>
                            <PersonIcon />
                        </ListItemIcon>
                        <ListItemText primary="Datos personales" />
                    </ListItemButton>
                </ListItem>
                <ListItem>
                    <ListItemButton>
                        <ListItemIcon>
                            <WorkIcon />
                        </ListItemIcon>
                        <ListItemText primary="Experiencia" />
                    </ListItemButton>
                </ListItem>
            </List>
        </div >
    )
}

export default ItemList
