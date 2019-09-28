# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 23:41:29 2018

@author: zhangx
"""

import numpy
import pylab

data = [(4.9,'2011/03/12 23:57:34'),
(4.9,'2011/03/12 23:53:45'),
(5.0,'2011/03/12 23:51:24'),
(5.2,'2011/03/12 23:40:49'),
(5.1,'2011/03/12 23:37:24'),
(6.1,'2011/03/12 23:24:50'),
(5.4,'2011/03/12 23:20:42'),
(3.0,'2011/03/12 23:12:18'),
(4.7,'2011/03/12 22:53:35'),
(4.8,'2011/03/12 22:42:39'),
(5.6,'2011/03/12 22:31:27'),
(6.3,'2011/03/12 22:12:46'),
(4.9,'2011/03/12 22:05:17'),
(4.5,'2011/03/12 21:58:40'),
(5.3,'2011/03/12 21:58:17'),
(5.5,'2011/03/12 21:48:09'),
(5.0,'2011/03/12 21:40:58'),
(5.0,'2011/03/12 21:38:35'),
(4.8,'2011/03/12 20:48:48'),
(4.9,'2011/03/12 20:41:25'),
(4.3,'2011/03/12 20:16:59'),
(5.2,'2011/03/12 20:09:55'),
(5.0,'2011/03/12 20:08:25'),
(4.8,'2011/03/12 19:59:01'),
(4.6,'2011/03/12 19:55:28'),
(5.0,'2011/03/12 19:45:19'),
(4.7,'2011/03/12 19:43:47'),
(4.8,'2011/03/12 19:38:08'),
(4.9,'2011/03/12 19:22:47'),
(5.1,'2011/03/12 19:11:59'),
(4.8,'2011/03/12 19:01:05'),
(4.5,'2011/03/12 18:51:37'),
(4.8,'2011/03/12 18:38:38'),
(5.0,'2011/03/12 18:28:39'),
(4.7,'2011/03/12 18:09:15'),
(4.7,'2011/03/12 17:59:57'),
(4.7,'2011/03/12 17:54:19'),
(4.8,'2011/03/12 17:51:27'),
(4.8,'2011/03/12 17:48:13'),
(4.8,'2011/03/12 17:40:56'),
(6.0,'2011/03/12 17:19:24'),
(5.1,'2011/03/12 17:13:02'),
(5.2,'2011/03/12 17:11:09'),
(5.1,'2011/03/12 17:01:22'),
(4.8,'2011/03/12 16:55:41'),
(4.7,'2011/03/12 16:48:14'),
(5.0,'2011/03/12 16:38:45'),
(4.9,'2011/03/12 16:36:41'),
(5.0,'2011/03/12 16:22:15'),
(4.8,'2011/03/12 16:19:05'),
(4.7,'2011/03/12 16:07:39'),
(4.8,'2011/03/12 16:03:56'),
(4.9,'2011/03/12 14:53:21'),
(5.7,'2011/03/12 14:43:09'),
(5.6,'2011/03/12 14:35:00'),
(4.9,'2011/03/12 14:14:56'),
(5.3,'2011/03/12 14:11:05'),
(5.8,'2011/03/12 14:03:30'),
(5.2,'2011/03/12 13:57:12'),
(5.3,'2011/03/12 13:26:56'),
(6.4,'2011/03/12 13:15:42'),
(5.8,'2011/03/12 12:53:50'),
(4.9,'2011/03/12 12:50:28'),
(4.9,'2011/03/12 12:43:13'),
(4.8,'2011/03/12 12:27:17'),
(4.9,'2011/03/12 12:15:31'),
(4.9,'2011/03/12 12:06:57'),
(4.3,'2011/03/12 12:06:16'),
(4.4,'2011/03/12 12:03:43'),
(5.7,'2011/03/12 11:46:01'),
(4.9,'2011/03/12 11:39:05'),
(4.9,'2011/03/12 11:20:16'),
(4.9,'2011/03/12 11:05:00'),
(6.1,'2011/03/12 10:53:31'),
(4.7,'2011/03/12 10:49:24'),
(5.0,'2011/03/12 10:39:12'),
(5.3,'2011/03/12 10:34:49'),
(5.5,'2011/03/12 10:20:22'),
(4.4,'2011/03/12 10:17:09'),
(4.9,'2011/03/12 10:06:12'),
(5.0,'2011/03/12 10:00:26'),
(5.2,'2011/03/12 09:51:35'),
(4.9,'2011/03/12 09:47:59'),
(5.1,'2011/03/12 09:40:44'),
(5.0,'2011/03/12 09:27:12'),
(5.4,'2011/03/12 09:18:56'),
(4.7,'2011/03/12 09:05:33'),
(5.2,'2011/03/12 09:00:03'),
(4.6,'2011/03/12 08:58:24'),
(5.0,'2011/03/12 08:52:50'),
(5.0,'2011/03/12 08:45:30'),
(5.0,'2011/03/12 08:38:40'),
(4.8,'2011/03/12 08:38:04'),
(4.9,'2011/03/12 08:30:22'),
(4.6,'2011/03/12 08:22:07'),
(5.0,'2011/03/12 08:13:42'),
(5.2,'2011/03/12 07:54:10'),
(4.8,'2011/03/12 07:50:54'),
(4.7,'2011/03/12 07:46:42'),
(4.9,'2011/03/12 07:38:06'),
(4.7,'2011/03/12 07:30:18'),
(4.9,'2011/03/12 07:21:00'),
(5.1,'2011/03/12 07:18:53'),
(5.1,'2011/03/12 07:13:35'),
(5.0,'2011/03/12 07:07:32'),
(4.7,'2011/03/12 07:02:21'),
(4.5,'2011/03/12 06:53:53'),
(4.8,'2011/03/12 06:49:12'),
(4.8,'2011/03/12 06:44:01'),
(4.8,'2011/03/12 06:39:26'),
(5.0,'2011/03/12 06:36:00'),
(4.9,'2011/03/12 06:29:10'),
(2.9,'2011/03/12 06:20:47'),
(5.5,'2011/03/12 06:18:43'),
(5.5,'2011/03/12 06:10:44'),
(5.1,'2011/03/12 06:10:23'),
(5.2,'2011/03/12 06:00:25'),
(5.1,'2011/03/12 05:58:59'),
(5.0,'2011/03/12 05:14:51'),
(5.3,'2011/03/12 04:52:58'),
(5.1,'2011/03/12 04:47:19'),
(5.0,'2011/03/12 04:43:04'),
(4.7,'2011/03/12 04:37:21'),
(5.2,'2011/03/12 04:06:09'),
(5.5,'2011/03/12 04:04:49'),
(5.1,'2011/03/12 03:54:48'),
(5.3,'2011/03/12 03:34:46'),
(5.3,'2011/03/12 03:29:28'),
(4.8,'2011/03/12 03:21:44'),
(5.7,'2011/03/12 03:11:59'),
(5.8,'2011/03/12 03:01:49'),
(5.6,'2011/03/12 02:47:36'),
(2.6,'2011/03/12 02:43:49'),
(5.0,'2011/03/12 02:43:11'),
(5.2,'2011/03/12 02:34:05'),
(4.8,'2011/03/12 02:27:50'),
(4.9,'2011/03/12 02:13:51'),
(4.9,'2011/03/12 02:07:21'),
(4.8,'2011/03/12 02:04:55'),
(5.2,'2011/03/12 01:59:44'),
(6.8,'2011/03/12 01:47:16'),
(6.2,'2011/03/12 01:46:21'),
(5.2,'2011/03/12 01:43:20'),
(6.0,'2011/03/12 01:34:10'),
(5.1,'2011/03/12 01:25:04'),
(6.1,'2011/03/12 01:19:07'),
(5.7,'2011/03/12 01:17:41'),
(5.4,'2011/03/12 01:17:02'),
(4.8,'2011/03/12 01:12:16'),
(5.1,'2011/03/12 01:03:59'),
(5.5,'2011/03/12 00:45:10'),
(5.0,'2011/03/12 00:39:37'),
(5.0,'2011/03/12 00:25:08'),
(5.0,'2011/03/12 00:21:25'),
(3.0,'2011/03/12 00:04:09'),   
(5.4,'2011/03/11 23:59:21'),
(5.3,'2011/03/11 23:58:04'),
(5.1,'2011/03/11 23:53:29'),
(5.1,'2011/03/11 23:40:12'),
(4.9,'2011/03/11 23:31:23'),
(5.3,'2011/03/11 23:26:51'),
(5.0,'2011/03/11 23:21:22'),
(4.9,'2011/03/11 23:05:15'),
(5.4,'2011/03/11 22:54:28'),
(5.8,'2011/03/11 22:51:18'),
(5.3,'2011/03/11 22:42:59'),
(5.0,'2011/03/11 22:36:57'),
(4.6,'2011/03/11 22:29:42'),
(4.9,'2011/03/11 22:22:36'),
(4.7,'2011/03/11 22:08:14'),
(2.9,'2011/03/11 22:01:26'),
(5.2,'2011/03/11 21:41:58'),
(4.8,'2011/03/11 21:34:25'),
(5.4,'2011/03/11 21:00:46'),
(5.1,'2011/03/11 20:41:24'),
(5.5,'2011/03/11 20:36:10'),
(5.1,'2011/03/11 20:34:40'),
(5.5,'2011/03/11 20:23:44'),
(6.3,'2011/03/11 20:11:23'),
(6.6,'2011/03/11 19:46:49'),
(3.2,'2011/03/11 19:46:27'),
(5.2,'2011/03/11 19:45:24'),
(5.5,'2011/03/11 19:31:56'),
(5.5,'2011/03/11 19:24:29'),
(6.1,'2011/03/11 19:02:59'),
(6.2,'2011/03/11 18:59:15'),
(4.9,'2011/03/11 18:55:15'),
(5.1,'2011/03/11 18:44:06'),
(4.9,'2011/03/11 18:43:14'),
(4.9,'2011/03/11 18:39:34'),
(5.9,'2011/03/11 18:17:06'),
(5.7,'2011/03/11 18:11:24'),
(4.7,'2011/03/11 18:02:39'),
(5.0,'2011/03/11 17:50:01'),
(5.4,'2011/03/11 17:32:14'),
(5.1,'2011/03/11 17:30:48'),
(5.0,'2011/03/11 17:23:57'),
(5.5,'2011/03/11 17:17:00'),
(4.8,'2011/03/11 17:15:00'),
(5.0,'2011/03/11 17:12:41'),
(5.0,'2011/03/11 16:55:53'),
(4.8,'2011/03/11 16:54:53'),
(5.0,'2011/03/11 16:34:22'),
(5.0,'2011/03/11 16:20:52'),
(5.5,'2011/03/11 16:11:27'),
(5.3,'2011/03/11 16:04:53'),
(5.0,'2011/03/11 15:55:23'),
(5.0,'2011/03/11 15:50:59'),
(5.0,'2011/03/11 15:46:02'),
(5.4,'2011/03/11 15:42:05'),
(4.9,'2011/03/11 15:36:16'),
(5.2,'2011/03/11 15:32:34'),
(5.6,'2011/03/11 15:19:38'),
(6.2,'2011/03/11 15:13:15'),
(5.0,'2011/03/11 15:01:39'),
(5.8,'2011/03/11 14:56:16'),
(5.4,'2011/03/11 14:54:04'),
(5.1,'2011/03/11 14:44:08'),
(5.4,'2011/03/11 14:26:31'),
(5.1,'2011/03/11 14:20:20'),
(2.6,'2011/03/11 14:18:29'),
(5.2,'2011/03/11 14:10:39'),
(5.5,'2011/03/11 14:00:38'),
(4.9,'2011/03/11 13:58:50'),
(5.2,'2011/03/11 13:55:28'),
(5.3,'2011/03/11 13:48:38'),
(5.6,'2011/03/11 13:43:10'),
(4.9,'2011/03/11 13:42:27'),
(5.6,'2011/03/11 13:34:36'),
(5.1,'2011/03/11 13:31:55'),
(2.5,'2011/03/11 13:21:37'),
(5.8,'2011/03/11 13:16:50'),
(5.1,'2011/03/11 13:15:45'),
(5.3,'2011/03/11 13:02:43'),
(5.3,'2011/03/11 12:59:21'),
(5.4,'2011/03/11 12:54:52'),
(5.6,'2011/03/11 12:49:01'),
(5.3,'2011/03/11 12:34:22'),
(5.2,'2011/03/11 12:33:19'),
(5.2,'2011/03/11 12:28:45'),
(5.3,'2011/03/11 12:24:37'),
(3.3,'2011/03/11 12:15:07'),
(5.9,'2011/03/11 12:12:53'),
(5.1,'2011/03/11 12:04:16'),
(5.5,'2011/03/11 11:56:16'),
(5.1,'2011/03/11 11:54:02'),
(5.8,'2011/03/11 11:46:47'),
(5.8,'2011/03/11 11:44:28'),
(6.5,'2011/03/11 11:36:39'),
(5.7,'2011/03/11 11:21:02'),
(5.5,'2011/03/11 11:16:51'),
(5.5,'2011/03/11 11:13:12'),
(5.5,'2011/03/11 11:10:58'),
(5.6,'2011/03/11 11:00:51'),
(5.1,'2011/03/11 10:58:06'),
(3.2,'2011/03/11 10:56:23'),
(5.0,'2011/03/11 10:52:08'),
(5.5,'2011/03/11 10:45:46'),
(5.3,'2011/03/11 10:35:36'),
(5.9,'2011/03/11 10:28:44'),
(5.6,'2011/03/11 10:20:27'),
(6.0,'2011/03/11 10:10:35'),
(5.2,'2011/03/11 09:59:57'),
(5.5,'2011/03/11 09:47:02'),
(2.5,'2011/03/11 09:45:08'),
(5.2,'2011/03/11 09:42:22'),
(5.4,'2011/03/11 09:37:08'),
(3.0,'2011/03/11 09:33:58'),
(2.9,'2011/03/11 09:24:53'),
(2.6,'2011/03/11 09:14:36'),
(2.6,'2011/03/11 09:10:26'),
(5.5,'2011/03/11 09:09:15'),
(2.8,'2011/03/11 09:05:22'),
(5.4,'2011/03/11 09:04:10'),
(2.5,'2011/03/11 09:03:56'),
(2.5,'2011/03/11 09:03:44'),
(3.3,'2011/03/11 09:03:38'),
(5.2,'2011/03/11 09:00:20'),
(4.6,'2011/03/11 08:58:26'),
(5.4,'2011/03/11 08:52:26'),
(5.5,'2011/03/11 08:46:48'),
(5.9,'2011/03/11 08:40:56'),
(6.1,'2011/03/11 08:31:08'),
(6.5,'2011/03/11 08:19:24'),
(6.2,'2011/03/11 08:15:41'),
(6.2,'2011/03/11 08:12:05'),
(5.5,'2011/03/11 08:10:31'),
(5.9,'2011/03/11 08:01:59'),
(5.6,'2011/03/11 07:56:16'),
(5.7,'2011/03/11 07:54:45'),
(5.8,'2011/03/11 07:42:55'),
(5.9,'2011/03/11 07:38:27'),
(4.4,'2011/03/11 07:36:12'),
(6.1,'2011/03/11 07:28:12'),
(6.1,'2011/03/11 07:25:33'),
(6.3,'2011/03/11 07:14:59'),
(5.9,'2011/03/11 07:13:47'),
(5.8,'2011/03/11 07:11:00'),
(6.3,'2011/03/11 06:57:15'),
(6.3,'2011/03/11 06:48:47'),
(7.1,'2011/03/11 06:25:51'),
(3.3,'2011/03/11 06:18:04'),
(6.8,'2011/03/11 06:15:40'),
(6.4,'2011/03/11 06:07:22'),
(6.4,'2011/03/11 06:06:11'),
(8.9,'2011/03/11 05:46:24'),
(3.4,'2011/03/11 04:51:25'),
(4.8,'2011/03/11 04:28:21'),
(4.5,'2011/03/11 04:05:41'),
(2.6,'2011/03/11 02:55:42'),
(2.9,'2011/03/11 02:52:08'),
(2.5,'2011/03/11 02:32:09'),
(2.8,'2011/03/11 01:02:00'),
(2.5,'2011/03/11 00:53:59'),
(4.0,'2011/03/11 00:25:29'),
(5.3,'2011/03/11 00:14:51'),
(4.9,'2011/03/10 22:44:26'),
(4.7,'2011/03/10 21:49:47'),
(2.8,'2011/03/10 20:49:08'),
(2.5,'2011/03/10 19:44:35'),
(5.0,'2011/03/10 19:06:11'),
(3.4,'2011/03/10 18:10:05'),
(6.5,'2011/03/10 17:08:37'),
(5.2,'2011/03/10 16:54:45'),
(3.2,'2011/03/10 15:56:25'),
(4.7,'2011/03/10 15:22:52'),
(4.7,'2011/03/10 14:30:34'),
(4.6,'2011/03/10 14:24:46'),
(2.7,'2011/03/10 13:45:34'),
(2.8,'2011/03/10 11:52:58'),
(5.1,'2011/03/10 11:21:08'),
(2.7,'2011/03/10 10:58:37'),
(5.2,'2011/03/10 09:02:22'),
(4.8,'2011/03/10 08:59:19'),
(5.7,'2011/03/10 08:08:21'),
(3.1,'2011/03/10 07:41:31'),
(4.8,'2011/03/10 07:33:04'),
(4.2,'2011/03/10 07:07:09'),
(3.2,'2011/03/10 06:19:01'),
(2.5,'2011/03/10 05:57:39'),
(2.5,'2011/03/10 05:01:11'),
(5.4,'2011/03/10 04:58:18'),
(4.6,'2011/03/10 04:26:48'),
(4.6,'2011/03/10 04:14:00'),
(2.8,'2011/03/10 02:34:17'),
(2.9,'2011/03/10 01:38:14'),
(5.0,'2011/03/10 01:20:24'),
(2.9,'2011/03/10 00:14:41'),   
(4.8,'2011/03/09 23:57:42'),
(5.4,'2011/03/09 23:37:01'),
(2.6,'2011/03/09 22:41:30'),
(2.6,'2011/03/09 22:17:41'),
(6.5,'2011/03/09 21:24:52'),
(6.1,'2011/03/09 21:22:18'),
(4.9,'2011/03/09 21:00:58'),
(3.5,'2011/03/09 20:48:31'),
(6.0,'2011/03/09 18:44:35'),
(2.5,'2011/03/09 18:28:33'),
(3.7,'2011/03/09 18:25:26'),
(6.1,'2011/03/09 18:16:15'),
(4.9,'2011/03/09 17:57:27'),
(2.5,'2011/03/09 17:02:06'),
(2.5,'2011/03/09 16:12:03'),
(2.8,'2011/03/09 14:30:37'),
(4.8,'2011/03/09 14:24:06'),
(5.3,'2011/03/09 13:57:28'),
(3.2,'2011/03/09 13:55:24'),
(5.1,'2011/03/09 13:51:42'),
(5.0,'2011/03/09 13:24:08'),
(2.8,'2011/03/09 12:56:35'),
(2.6,'2011/03/09 12:14:14'),
(4.7,'2011/03/09 12:03:18'),
(5.1,'2011/03/09 11:27:52'),
(3.5,'2011/03/09 11:05:09'),
(4.7,'2011/03/09 10:13:40'),
(2.6,'2011/03/09 09:45:14'),
(4.8,'2011/03/09 08:55:38'),
(3.3,'2011/03/09 08:37:30'),
(5.3,'2011/03/09 08:02:36'),
(5.1,'2011/03/09 07:56:28'),
(5.0,'2011/03/09 07:13:48'),
(5.1,'2011/03/09 06:25:12'),
(4.9,'2011/03/09 06:12:13'),
(2.9,'2011/03/09 05:33:50'),
(4.7,'2011/03/09 05:27:06'),
(5.3,'2011/03/09 04:45:54'),
(5.7,'2011/03/09 04:37:04'),
(5.2,'2011/03/09 04:32:10'),
(3.0,'2011/03/09 04:17:17'),
(4.8,'2011/03/09 04:15:39'),
(5.2,'2011/03/09 04:05:54'),
(2.5,'2011/03/09 03:51:21'),
(5.0,'2011/03/09 03:19:00'),
(5.2,'2011/03/09 03:08:36'),
(5.6,'2011/03/09 02:57:17'),
(7.2,'2011/03/09 02:45:20'),
(4.6,'2011/03/09 01:47:47'),
(4.7,'2011/03/09 01:30:27')]

ydata = []

for t in data:
	ydata.append(t[0])

pylab.plot(ydata)
pylab.title('Earthquake Magnitude in Japan in 20111 from 3/9-3/12')
pylab.xlabel('Time')
pylab.ylabel('Magnitude')
pylab.show()