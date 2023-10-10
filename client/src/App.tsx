import "./index.css"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import OwnerSignUp from "./pages/OwnerSignUp"
import Hirirum from "./pages/Hirirum"
import Hub from "./pages/Hub"
import OwnerSignIn from "./pages/OwnerSignIn"

function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Hirirum/>}/>
      <Route path="/Owner/SignUp" element={<OwnerSignUp/>}/>
      <Route path="/Owner/SignIn" element={<OwnerSignIn/>}/>
      <Route path="/Hub" element={<Hub/>}/>
    </Routes>
    </BrowserRouter>
  )
}

export default App

