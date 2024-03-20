-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-03-2024 a las 14:16:12
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agenda2024`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `canciones`
--

CREATE TABLE `canciones` (
  `id_canciones` int(11) NOT NULL,
  `titulo` varchar(60) NOT NULL,
  `artista` varchar(60) NOT NULL,
  `genero` varchar(60) NOT NULL,
  `precio` varchar(60) NOT NULL,
  `duracion` varchar(12) NOT NULL,
  `lanzamiento` varchar(60) NOT NULL,
  `img` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compras`
--

CREATE TABLE `compras` (
  `id_compra` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `precio` decimal(10,0) NOT NULL,
  `met_pago` varchar(10) NOT NULL,
  `polper` int(11) NOT NULL,
  `id_canciones` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------
use agenda2024;
select*from personas;
--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `polper` int(11) NOT NULL,
  `nombrep` varchar(60) NOT NULL,
  `apellidop` varchar(60) NOT NULL,
  `emailp` varchar(60) NOT NULL,
  `dirp` varchar(60) NOT NULL,
  `telp` varchar(12) NOT NULL,
  `usup` varchar(60) NOT NULL,
  `passp` varchar(255) NOT NULL
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE personas ADD roles varchar(25) NOT NULL;
--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`polper`, `nombrep`, `apellidop`, `emailp`, `dirp`, `telp`, `usup`, `passp`) VALUES
(3, 'Juana', 'sadf', 'juanita@juana.com', 'dsfsdf', '8745189', 'hola.cc', 'Encriptado: scrypt:32768:8:1$pfzcJtu4587wbn71$b2f6c2e32d3fe7ee72db4f31d68fbf06b64325e2b1122097445139e72fd5b947a119f533cf78ff8a8dc8549ad37f6b12e2474f46cb56350391d7b07dc8c93569 | coincide:True'),
(4, 'lorena', 'casa', 'gian@hmma.com', 'ASA', '123456', 'LORENA.1', 'Encriptado: scrypt:32768:8:1$b20Gs9BxmITWT0m4$b5e3fe8b8e139275cde40cc48e62d7f2e07d93b8ef72ce81e4334a1ac6de95b2e96c5789930dd587d406df0e9a012005e94e9e08a99c07deb05fa25585bcb5a3 | coincide:True'),
(5, 'Johanna', 'Cifuentes', 'cifuetnes0903@gmail.com', 'sena', '89456', 'cifuentes0903', 'scrypt:32768:8:1$x21p0c8j2Hwxw49G$cae2b5ce15ffd8027dfaea5fca2a1d1323af47fb20ca86092028c74ac955f939e58773e2f54e65f36a3fde621756ed5c143666e2b176251d477334922f307ca7'),
(6, 'Johanna', 'Cifuentes', 'cifuetnes0903@gmail.com', 'sena', '89456', 'cifuentes0903', 'scrypt:32768:8:1$ubLJYynBjfsUEMqc$244f108d986797269cbed43e413b5ad9a8e3e53cff69e91d0222ca9169bab01d0524481ce150a72ef88b419af86563ab9675323e98dc41c728bf5959a2cdc7ef');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usu` int(11) NOT NULL,
  `nombreusu` date NOT NULL,
  `apellidousu` decimal(10,0) NOT NULL,
  `emailusu` varchar(10) NOT NULL,
  `dirusu` varchar(10) NOT NULL,
  `telusu` varchar(10) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `contraseña` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `canciones`
--
ALTER TABLE `canciones`
  ADD PRIMARY KEY (`id_canciones`);

--
-- Indices de la tabla `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`id_compra`),
  ADD KEY `polper` (`polper`),
  ADD KEY `id_canciones` (`id_canciones`);

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`polper`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usu`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `compras`
--
ALTER TABLE `compras`
  MODIFY `id_compra` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `personas`
--
ALTER TABLE `personas`
  MODIFY `polper` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usu` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `compras`
--
ALTER TABLE `compras`
  ADD CONSTRAINT `compras_ibfk_1` FOREIGN KEY (`polper`) REFERENCES `personas` (`polper`),
  ADD CONSTRAINT `compras_ibfk_2` FOREIGN KEY (`id_canciones`) REFERENCES `canciones` (`id_canciones`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
