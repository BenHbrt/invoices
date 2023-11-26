import './User.scss';

import { useContext, useState } from 'react';
import { UserContext } from '../App';

const User = () => {

    const { user, setUser } = useContext(UserContext);

    const [hover, setHover] = useState(false)

    return (
        <div
        className="user"
        onMouseEnter={() => setHover(true)}
        onMouseLeave={() => setHover(false)}
        >
            <img src={require("../img/icons/account.png")} alt="icon" />
            <span>{user.username}</span>
            {hover ?
            <ul className="user_menu">
                <li>
                    <img src={require("../img/icons/logout.png")} alt="logo" />
                    <span>Logout</span>
                </li>
            </ul> : null}
        </div>
    );
};

export default User;