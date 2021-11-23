import React from 'react'
import { List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import WorkIcon from '@mui/icons-material/Work';
import SchoolIcon from '@mui/icons-material/School';
import BuildIcon from '@mui/icons-material/Build';
import { Link as RouterLink } from 'react-router-dom';

const ItemList = () => {
    return (
        <div>
            <List>
                <ListItem button component={RouterLink} to="/profile-resume">
                    <ListItemIcon>
                        <PersonIcon />
                    </ListItemIcon>
                    <ListItemText primary="Datos personales" />
                </ListItem>

                <ListItem button component={RouterLink} to="/profile-resume/experience">
                    <ListItemIcon>
                        <WorkIcon />
                    </ListItemIcon>
                    <ListItemText primary="Experiencia" />
                </ListItem>
                <ListItem button>
                    <ListItemIcon>
                        <SchoolIcon />
                    </ListItemIcon>
                    <ListItemText primary="Educación" />
                </ListItem>
                <ListItem button>
                    <ListItemIcon>
                        <BuildIcon />
                    </ListItemIcon>
                    <ListItemText primary="Habilidades" />
                </ListItem>
            </List>
        </div >
    )
}

export default ItemList
