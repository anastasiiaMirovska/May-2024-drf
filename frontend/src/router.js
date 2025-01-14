import MainLayout from "./layouts/MainLayout";
import {createBrowserRouter, Navigate} from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import PizzasPage from "./pages/PizzasPage";

const router = createBrowserRouter(
    [
        {
            path: '', element: <MainLayout/>, children: [
                {
                    index:true, element: <Navigate to={'login'}/>
                },
                {
                    path: 'login', element: <LoginPage/>
                },
                {
                    path: 'pizzas', element: <PizzasPage/>
                }
            ]
        }
    ]
)
export {
    router
}
