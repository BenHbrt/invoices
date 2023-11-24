import { useContext } from 'react';
import { UserContext } from '../App';

const User = () => {

    const { user, setUser } = useContext(UserContext);

    return (
        <div className="user">
            {user.username}
        </div>
    );
};

export default User;