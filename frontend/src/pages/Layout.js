import { Outlet } from 'react-router-dom';
import { useContext } from 'react';
import { UserContext } from '../App';

import User from '../components/User';

const Layout = () => {

    const { user, setUser } = useContext(UserContext)

    return (
        <>
        <header>
            <span>Invoices</span>
            {user ? <User /> : null}
        </header>
        <div>
            Layout
            <button onClick={() => setUser(!user)}>Change</button>
            <button onClick={() => console.table(user)}>User Data</button>
            <Outlet />
        </div>
        </>
    );
};

export default Layout;