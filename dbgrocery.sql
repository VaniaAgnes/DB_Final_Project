-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 27, 2023 at 07:42 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbgrocery`
--

-- --------------------------------------------------------

--
-- Table structure for table `brand`
--

CREATE TABLE `brand` (
  `BrandID` varchar(50) NOT NULL,
  `BrandName` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `brand`
--

INSERT INTO `brand` (`BrandID`, `BrandName`) VALUES
('B0001', 'Indofood Group '),
('B0002', 'Sinar Mas Agro Resources'),
('B0003', 'Mayora Group'),
('B0004', 'Indofood CBP Sukses Makmur'),
('B0005', 'Wings Group (Export Presence)'),
('B0006', 'Unilever (Import Group)'),
('B0007', 'Nestle (Import Group)'),
('B0008', 'Coca-Cola (Import Group)'),
('B0009', 'PepsiCo (Import Group)'),
('B0010', 'Indofood Snack Foods'),
('B0011', 'GarudaFood Group'),
('B0012', 'Mondelez International');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `CategoryID` varchar(50) NOT NULL,
  `CategoryName` varchar(50) DEFAULT NULL,
  `CategoryDetails` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`CategoryID`, `CategoryName`, `CategoryDetails`) VALUES
('C0001', 'Instant Food', 'Indomie Goreng Mi Instan 85g '),
('C0002', 'Instant Food', 'Indomie Mie Kari Ayam 69g'),
('C0003', 'Instant Food', 'Supermi Kaldu Ayam Mie Instant 60g'),
('C0004', 'Cooking Supplies', 'Filma Minyak Goreng 2L'),
('C0005', 'Cooking Supplies', 'Filma Margarine Bernutrisi 200g'),
('C0006', 'Snacks', 'Roma Malkist Crackers 250g'),
('C0007', 'Snacks', 'Roma Malkist Belgian Style Chocolate Crackers 250g'),
('C0008', 'Instant Food', 'Energen Cereal Instant Rasa Vanilla 10x29g'),
('C0009', 'Beverages', 'Indomilk Kids Strawberry Milk 115ml'),
('C0010', 'Beverages', 'Indomilk Full Cream Milk 250ml'),
('C0011', 'Snacks', 'Qtela Cassava Chips Original 185g'),
('C0012', 'Snacks', 'Qtela Cassava Chips Balado 60g'),
('C0013', 'Instant Food', 'Mi Sedaap Instant Goreng Cup 85g'),
('C0014', 'Cleaning Supplies', 'So Klin Detergent Purple Lavender 800g'),
('C0015', 'Health and Beauty', 'Pepsodent White 180gr'),
('C0016', 'Health and Beauty', 'Lifebuoy Body Wash Total 10 500ml'),
('C0017', 'Beverages', 'Nestle Pure Life Mineral Water 660ml'),
('C0018', 'Beverages', 'Coca Cola Can 250ml'),
('C0019', 'Beverages', 'Coca Cola Bottle 390ml'),
('C0020', 'Snacks', 'Lays Potato Chips Seaweed 120g'),
('C0021', 'Beverages', 'Pepsi Bottle Drink 600ml'),
('C0022', 'Snacks', 'Chitato Potato Chips Sapi Panggang Flavour 68gr'),
('C0023', 'Snacks', 'Taro Snacks Seaweed 10gr'),
('C0024', 'Snacks', 'Gery Chocolate Wafer 340gr'),
('C0025', 'Snacks', 'Oreo Double Stuff 147gr'),
('C0026', 'Candy', 'Cadbury Chocolate Dairy Milk 90gr');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `EmployeeID` varchar(50) NOT NULL,
  `EmployeeName` varchar(100) NOT NULL,
  `Position` varchar(50) NOT NULL,
  `ContactInformation` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`EmployeeID`, `EmployeeName`, `Position`, `ContactInformation`) VALUES
('E0001', 'Abdullah', 'Manager', '0814567283'),
('E0002', 'Michelle', 'Cashier', '0810514704488'),
('E0003', 'Bessie', 'Part Time Cashier ', '081293389167'),
('E0004', 'Rafi', 'Cashier', '0810514704485'),
('E0005', 'Prada', 'Part Time Worker', '08114220164');

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `InventoryID` varchar(50) NOT NULL,
  `ProductID` varchar(50) DEFAULT NULL,
  `StockQuantity` int(50) DEFAULT NULL,
  `RestockDate` date DEFAULT NULL,
  `ShelfLocation` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`InventoryID`, `ProductID`, `StockQuantity`, `RestockDate`, `ShelfLocation`) VALUES
('I0001', 'P0001', 250, '2023-12-01', 'Aisle 1'),
('I0002', 'P0002', 150, '2023-12-01', 'Aisle 1'),
('I0003', 'P0003', 75, '2023-12-01', 'Aisle 1'),
('I0004', 'P0004', 50, '2023-12-03', 'Aisle 2'),
('I0005', 'P0005', 20, '2023-12-03', 'Aisle 2'),
('I0006', 'P0006', 30, '2023-12-10', 'Aisle 3'),
('I0007', 'P0007', 20, '2023-12-10', 'Aisle 3'),
('I0008', 'P0008', 15, '2023-12-01', 'Aisle 1'),
('I0009', 'P0009', 20, '2023-12-06', 'Aisle 4'),
('I0010', 'P0010', 40, '2023-12-06', 'Aisle 4'),
('I0011', 'P0011', 25, '2023-12-10', 'Aisle 3'),
('I0012', 'P0012', 25, '2023-12-10', 'Aisle 3'),
('I0013', 'P0013', 100, '2023-12-01', 'Aisle 1'),
('I0014', 'P0014', 30, '2023-12-07', 'Aisle 5'),
('I0015', 'P0015', 35, '2023-12-05', 'Aisle 6'),
('I0016', 'P0016', 10, '2023-12-05', 'Aisle 6'),
('I0017', 'P0017', 200, '2023-12-06', 'Aisle 4'),
('I0018', 'P0018', 50, '2023-12-06', 'Aisle 4'),
('I0019', 'P0019', 75, '2023-12-06', 'Aisle 4'),
('I0020', 'P0020', 50, '2023-12-10', 'Aisle 3'),
('I0021', 'P0021', 45, '2023-12-06', 'Aisle 4'),
('I0022', 'P0022', 55, '2023-12-10', 'Aisle 3'),
('I0023', 'P0023', 10, '2023-12-10', 'Aisle 3'),
('I0024', 'P0024', 24, '2023-12-10', 'Aisle 3'),
('I0025', 'P0025', 40, '2023-12-10', 'Aisle 3'),
('I0026', 'P0026', 30, '2023-12-02', 'Aisle 7');

-- --------------------------------------------------------

--
-- Table structure for table `itempurchased`
--

CREATE TABLE `itempurchased` (
  `PurchasedID` varchar(50) NOT NULL,
  `TransactionID` varchar(50) NOT NULL,
  `ProductID` varchar(50) NOT NULL,
  `PurchasedQuantity` int(50) NOT NULL,
  `PurchasedPrice` int(50) NOT NULL,
  `TimeStamp` time(6) NOT NULL,
  `Subtotal` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `itempurchased`
--

INSERT INTO `itempurchased` (`PurchasedID`, `TransactionID`, `ProductID`, `PurchasedQuantity`, `PurchasedPrice`, `TimeStamp`, `Subtotal`) VALUES
('PS0001', 'T0001', 'P0001', 5, 3000, '15:20:07.000000', 15000),
('PS0002', 'T0001', 'P0004', 2, 40000, '15:20:07.000000', 80000),
('PS0003', 'T0001', 'P0007', 1, 13000, '15:20:07.000000', 13000),
('PS0004', 'T0001', 'P0017', 40, 5000, '15:20:07.000000', 200000),
('PS0005', 'T0002', 'P0009', 2, 4500, '10:41:33.000000', 9000),
('PS0006', 'T0002', 'P0012', 5, 10000, '10:41:33.000000', 50000),
('PS0007', 'T0002', 'P0019', 10, 8000, '10:41:33.000000', 80000),
('PS0008', 'T0002', 'P0025', 2, 11000, '10:41:33.000000', 22000),
('PS0009', 'T0003', 'P0008', 3, 25000, '20:05:11.000000', 75000),
('PS0010', 'T0003', 'P0014', 5, 25000, '20:05:11.000000', 125000),
('PS0011', 'T0003', 'P0013', 2, 5500, '20:05:11.000000', 11000),
('PS0012', 'T0004', 'P0023', 6, 6000, '12:30:44.000000', 36000),
('PS0013', 'T0004', 'P0020', 15, 12000, '12:30:44.000000', 180000),
('PS0014', 'T0004', 'P0015', 3, 22000, '12:30:44.000000', 66000),
('PS0015', 'T0004', 'P0010', 4, 7000, '12:30:44.000000', 28000),
('PS0016', 'T0005', 'P0016', 2, 47000, '17:14:27.000000', 94000),
('PS0017', 'T0005', 'P0007', 5, 9000, '17:14:27.000000', 45000),
('PS0018', 'T0005', 'P0005', 2, 10000, '17:14:27.000000', 20000),
('PS0019', 'T0005', 'P0003', 10, 3500, '17:14:27.000000', 35000);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `ProductID` varchar(50) NOT NULL,
  `BrandID` varchar(50) NOT NULL,
  `CategoryID` varchar(50) NOT NULL,
  `ProductName` varchar(100) NOT NULL,
  `Price` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`ProductID`, `BrandID`, `CategoryID`, `ProductName`, `Price`) VALUES
('P0001', 'B0001', 'C0001', 'Indomie', 3000),
('P0002', 'B0001', 'C0002', 'Indomie', 3000),
('P0003', 'B0001', 'C0003', 'Supermi', 3500),
('P0004', 'B0002', 'C0004', 'Filma', 40000),
('P0005', 'B0002', 'C0005', 'Filma', 10000),
('P0006', 'B0003', 'C0006', 'Roma Malkist', 13000),
('P0007', 'B0003', 'C0007', 'Roma Malkist', 9000),
('P0008', 'B0003', 'C0008', 'Energen', 25000),
('P0009', 'B0004', 'C0009', 'Indomilk Kids', 4500),
('P0010', 'B0004', 'C0010', 'Indomilk', 7000),
('P0011', 'B0004', 'C0011', 'Qtela', 18000),
('P0012', 'B0004', 'C0012', 'Qtela', 10000),
('P0013', 'B0005', 'C0013', 'Mi Sedaap', 5500),
('P0014', 'B0005', 'C0014', 'So Klin', 25000),
('P0015', 'B0006', 'C0015', 'Pepsodent', 22000),
('P0016', 'B0006', 'C0016', 'Lifebuoy', 47000),
('P0017', 'B0007', 'C0017', 'Pure Life', 5000),
('P0018', 'B0008', 'C0018', 'Coca-Cola', 6000),
('P0019', 'B0008', 'C0019', 'Coca-Cola', 8000),
('P0020', 'B0009', 'C0020', 'Lays', 12000),
('P0021', 'B0009', 'C0021', 'Pepsi', 15000),
('P0022', 'B0010', 'C0022', 'Chitato', 13000),
('P0023', 'B0010', 'C0023', 'Taro Snacks', 6000),
('P0024', 'B0011', 'C0024', 'Gery', 4500),
('P0025', 'B0012', 'C0025', 'Oreo', 11000),
('P0026', 'B0012', 'C0026', 'Dairy Milk', 17000);

-- --------------------------------------------------------

--
-- Table structure for table `salestransaction`
--

CREATE TABLE `salestransaction` (
  `TransactionID` varchar(50) NOT NULL,
  `EmployeeID` varchar(50) DEFAULT NULL,
  `TransactionDate` date NOT NULL,
  `TotalAmount` int(11) NOT NULL,
  `PaymentStatus` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `salestransaction`
--

INSERT INTO `salestransaction` (`TransactionID`, `EmployeeID`, `TransactionDate`, `TotalAmount`, `PaymentStatus`) VALUES
('T0001', 'E0001', '2023-12-17', 308000, 'Successful'),
('T0002', 'E0001', '2023-12-19', 161000, 'Successful'),
('T0003', 'E0004', '2023-12-25', 211000, 'Successful'),
('T0004', 'E0005', '2023-12-20', 310000, 'Successful'),
('T0005', 'E0002', '2023-12-18', 194000, 'Successful');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`BrandID`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`CategoryID`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`EmployeeID`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`InventoryID`),
  ADD KEY `InventoryProductID` (`ProductID`);

--
-- Indexes for table `itempurchased`
--
ALTER TABLE `itempurchased`
  ADD PRIMARY KEY (`PurchasedID`),
  ADD KEY `TransactionID` (`TransactionID`),
  ADD KEY `ProductID` (`ProductID`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`ProductID`),
  ADD KEY `BrandID` (`BrandID`),
  ADD KEY `CategoryID` (`CategoryID`);

--
-- Indexes for table `salestransaction`
--
ALTER TABLE `salestransaction`
  ADD PRIMARY KEY (`TransactionID`),
  ADD KEY `EmployeeID` (`EmployeeID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `inventory`
--
ALTER TABLE `inventory`
  ADD CONSTRAINT `InventoryProductID` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`);

--
-- Constraints for table `itempurchased`
--
ALTER TABLE `itempurchased`
  ADD CONSTRAINT `ProductID` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`),
  ADD CONSTRAINT `TransactionID` FOREIGN KEY (`TransactionID`) REFERENCES `salestransaction` (`TransactionID`);

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `BrandID` FOREIGN KEY (`BrandID`) REFERENCES `brand` (`BrandID`),
  ADD CONSTRAINT `CategoryID` FOREIGN KEY (`CategoryID`) REFERENCES `category` (`CategoryID`);

--
-- Constraints for table `salestransaction`
--
ALTER TABLE `salestransaction`
  ADD CONSTRAINT `EmployeeID` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
