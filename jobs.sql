-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 01, 2017 at 01:50 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jobs`
--

-- --------------------------------------------------------

--
-- Table structure for table `job`
--

CREATE TABLE `job` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `company` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cover` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `job`
--

INSERT INTO `job` (`id`, `title`, `company`, `description`, `created`, `cover`) VALUES
(1, 'Drivers', 'waheguru and sons', '<p>Begins After struggling with this problem I took three steps: 1. Use JQuery versions anywhere between 1.9.0 and 3.0.0 2. Declare the JQuery file before declaring the Bootstrap file 3. Declare these two script files at the bottom of the tags rather than in the . These worked for me but there may be different behaviors based on the browser you are using.</p>', '2017-08-31 18:18:53', ''),
(2, 'pilot', 'kenaya airwigs', '<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry&#39;s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>', '2017-08-28 18:04:55', ''),
(3, 'Teacher', 'Huli School', '<p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using &#39;Content here, content here&#39;, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for &#39;lorem ipsum&#39; will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</p>', '2017-08-31 17:05:21', '');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(100) NOT NULL,
  `register_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `username`, `password`, `register_date`) VALUES
(1, 'susan', 'susan@gmail.com', 'susa', '$5$rounds=535000$zZivBnHHYAnKtp9W$tYTYzrCbOXbGfAEf1R4kyLkAktpGKEQ0khQAtm4ZMB.', '2017-08-26 20:28:31'),
(2, 'Joe', 'benja@gmail.com', 'jowe', '$5$rounds=535000$wTD.x1tSooV3nYlN$ZDBm9jz5MSplQGyOz8w5brwIe9aQQby0btwnIySmtW7', '2017-08-26 20:29:13'),
(3, 'Joe', 'benja@gmail.com', 'stella', '$5$rounds=535000$7kber4y29erwwkqa$aWUioqRrTo3VHFonVg7CgcStd5upYqzQ3GtH5gSuqMA', '2017-08-26 20:29:56'),
(4, 'hemoo', 'benja@gmail.com', 'jowe', '$5$rounds=535000$3WtZyS7tmNNoep84$nAnMGQHVGUaejquEtPjS9rurOtdJjVAiSCu/2PA14qB', '2017-08-26 21:18:29'),
(5, 'huli', 'huli@gmail.com', 'huli', '$5$rounds=535000$gOx/jl9u7XX4CqZH$/HoPnO1JErvLxF6EAZutQQQAPKh1hdw7hBg.69dV1c/', '2017-08-28 08:48:02');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `job`
--
ALTER TABLE `job`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `job`
--
ALTER TABLE `job`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
