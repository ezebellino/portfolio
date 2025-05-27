import React from 'react'
import { Link } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css'
import { Navbar as BSNavbar, Nav, Container } from 'react-bootstrap'

const Navbar = () => (
  <BSNavbar bg="dark" variant="dark" expand="lg">
    <Container>
      <BSNavbar.Brand as={Link} to="/">Mi Portfolio</BSNavbar.Brand>
      <BSNavbar.Toggle aria-controls="basic-navbar-nav" />
      <BSNavbar.Collapse id="basic-navbar-nav">
        <Nav className="me-auto">
          <Nav.Link as={Link} to="/">Inicio</Nav.Link>
          <Nav.Link as={Link} to="/sobre-mi">Sobre mí</Nav.Link>
          <Nav.Link as={Link} to="/proyectos">Proyectos</Nav.Link>
          <Nav.Link as={Link} to="/contacto">Contacto</Nav.Link>
        </Nav>
      </BSNavbar.Collapse>
    </Container>
  </BSNavbar>
)

export default Navbar