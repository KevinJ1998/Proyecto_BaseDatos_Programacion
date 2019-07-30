-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-07-2019 a las 00:35:21
-- Versión del servidor: 10.3.16-MariaDB
-- Versión de PHP: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `prueba`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cuenta`
--

CREATE TABLE `cuenta` (
  `passwd_cuenta` varchar(30) DEFAULT NULL,
  `nombre_usuario` varchar(20) NOT NULL,
  `id_usuario` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cuenta`
--

INSERT INTO `cuenta` (`passwd_cuenta`, `nombre_usuario`, `id_usuario`) VALUES
('luis', 'Luis', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cuenta_prof`
--

CREATE TABLE `cuenta_prof` (
  `id_usuario_prof` int(3) NOT NULL,
  `nombre_cuenta_prof` varchar(20) NOT NULL,
  `passwd_cuenta_prof` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cuenta_prof`
--

INSERT INTO `cuenta_prof` (`id_usuario_prof`, `nombre_cuenta_prof`, `passwd_cuenta_prof`) VALUES
(2, 'Andres', 'andres'),
(4, 'Juan', 'Zaldumbide'),
(5, 'Luis', 'Ponce');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `id_est` int(10) NOT NULL,
  `nom_est` varchar(20) NOT NULL,
  `apel_est` varchar(20) DEFAULT NULL,
  `CI_est` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `estudiante`
--

INSERT INTO `estudiante` (`id_est`, `nom_est`, `apel_est`, `CI_est`) VALUES
(1, 'Kevin', 'Segovia', '1723707624'),
(2, 'Sebastian', 'Morales', '1706677281'),
(3, 'Nicole', 'Zambrano', '1723261232'),
(4, 'Jonathan', 'Vazquez', '1787652411'),
(5, 'Chantal', 'Morales', '1787165498'),
(13, 'Javier', NULL, NULL),
(14, 'Luis', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `est_mat`
--

CREATE TABLE `est_mat` (
  `id_mat` int(10) NOT NULL,
  `id_est` int(10) NOT NULL,
  `nota` decimal(2,1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `est_mat`
--

INSERT INTO `est_mat` (`id_mat`, `id_est`, `nota`) VALUES
(1, 1, '8.0'),
(2, 4, '6.0'),
(4, 3, '7.5'),
(6, 2, '9.2'),
(3, 5, '6.6'),
(3, 3, '5.5'),
(1, 4, '9.5'),
(3, 5, '7.0'),
(5, 1, '7.0'),
(2, 13, '8.9');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materia`
--

CREATE TABLE `materia` (
  `id_mat` int(10) NOT NULL,
  `nom_mat` varchar(20) NOT NULL,
  `credit_mat` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `materia`
--

INSERT INTO `materia` (`id_mat`, `nom_mat`, `credit_mat`) VALUES
(1, 'Calculo', 6),
(2, 'Fisica', 3),
(3, 'Programacion', 4),
(4, 'Sistemas_Operativos', 3),
(5, 'CAD', 3),
(6, 'Contabilidad', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesor`
--

CREATE TABLE `profesor` (
  `id_prof` int(10) NOT NULL,
  `nom_prof` varchar(20) NOT NULL,
  `apel_prof` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `profesor`
--

INSERT INTO `profesor` (`id_prof`, `nom_prof`, `apel_prof`) VALUES
(1, 'Juan', 'Zaldumbide'),
(2, 'Angel', 'Villota'),
(3, 'Alfonso', 'Boada'),
(4, 'Freddy', 'Llulluna'),
(5, 'Leandro', 'Pazmino'),
(6, 'Byron', 'Loarte'),
(10, 'Andres', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prof_mat`
--

CREATE TABLE `prof_mat` (
  `id_mat` int(10) NOT NULL,
  `id_prof` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `prof_mat`
--

INSERT INTO `prof_mat` (`id_mat`, `id_prof`) VALUES
(1, 2),
(2, 5),
(3, 1),
(4, 6),
(5, 4),
(6, 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cuenta`
--
ALTER TABLE `cuenta`
  ADD PRIMARY KEY (`id_usuario`);

--
-- Indices de la tabla `cuenta_prof`
--
ALTER TABLE `cuenta_prof`
  ADD PRIMARY KEY (`id_usuario_prof`);

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`id_est`);

--
-- Indices de la tabla `est_mat`
--
ALTER TABLE `est_mat`
  ADD KEY `FK_id_est` (`id_est`),
  ADD KEY `FK_id_mat` (`id_mat`);

--
-- Indices de la tabla `materia`
--
ALTER TABLE `materia`
  ADD PRIMARY KEY (`id_mat`);

--
-- Indices de la tabla `profesor`
--
ALTER TABLE `profesor`
  ADD PRIMARY KEY (`id_prof`);

--
-- Indices de la tabla `prof_mat`
--
ALTER TABLE `prof_mat`
  ADD KEY `FK_id_mat` (`id_mat`),
  ADD KEY `FK_id_prof` (`id_prof`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cuenta`
--
ALTER TABLE `cuenta`
  MODIFY `id_usuario` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `cuenta_prof`
--
ALTER TABLE `cuenta_prof`
  MODIFY `id_usuario_prof` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  MODIFY `id_est` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `materia`
--
ALTER TABLE `materia`
  MODIFY `id_mat` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `profesor`
--
ALTER TABLE `profesor`
  MODIFY `id_prof` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `est_mat`
--
ALTER TABLE `est_mat`
  ADD CONSTRAINT `est_mat_ibfk_1` FOREIGN KEY (`id_est`) REFERENCES `estudiante` (`id_est`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `est_mat_ibfk_2` FOREIGN KEY (`id_mat`) REFERENCES `materia` (`id_mat`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `prof_mat`
--
ALTER TABLE `prof_mat`
  ADD CONSTRAINT `prof_mat_ibfk_1` FOREIGN KEY (`id_mat`) REFERENCES `materia` (`id_mat`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `prof_mat_ibfk_2` FOREIGN KEY (`id_prof`) REFERENCES `profesor` (`id_prof`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
