USE PortfolioProject

SET ARITHABORT OFF 
SET ANSI_WARNINGS OFF

select * 
from PortfolioProject..CovidDeaths
where continent is not null
order by 3,4

select * 
from PortfolioProject..CovidVaccination
order by 3,4

select * from CovidDeaths

-- The Data that going to use

select location, date, total_cases, new_cases, total_deaths, population
from PortfolioProject..CovidDeaths
order by 1,2 



--Looking Total cases Vs Total Deaths
--Shows likelihood of dying if you contract covid in your country

select distinct(location)
from PortfolioProject..CovidDeaths

Select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
from PortfolioProject..CovidDeaths
where location = 'India'
and continent is not null
order by 1,2 



--Looking at Total Case Vs Population
--Show what percentage of population got infected

select location, date, population, total_cases,(total_cases/population)*100 as InfectedPercentage
from PortfolioProject..CovidDeaths
--where location ='India'
Where continent is not null
order by 1,2



-- Countries with Highest Infection Rate compared to Population

select Location,Population, max(total_cases) as HighestInfection, max((total_cases/population))*100 as Infected_Percentage
from PortfolioProject..CovidDeaths
--Where location = 'India'
Where continent is not null
group by location,population
order by Infected_Percentage desc



--Showing Countries with Highest Death Count per Population

select location,MAX(CAST(total_Deaths as int)) as TotalDeathCount
from PortfolioProject..CovidDeaths
--where location = 'India'
Where continent is not null
Group by location
Order by TotalDeathCount desc



--LET'S BREAK THINGS DOWN BY CONTINENT
--Showing continents with the Highest Death Count per Population

Select continent, MAX(cast(total_deaths as int)) as TotalDeathCount
from PortfolioProject..CovidDeaths
--Where location = 'India'
Where continent is not null
Group by continent
Order by TotalDeathCount Desc



--GLOBAL NUMBERS

Select date, SUM(new_cases) as Total_cases, SUM(Cast(new_deaths as int)) as Total_Deaths, SUM(CAST(new_deaths as int))/SUM(new_cases)*100 as Death_Percentage 
from PortfolioProject..CovidDeaths
--Where location = 'India'
where continent is not null
Group by date
Order by 1,2



--Looking at Total Death Percentage of World's Population

Select SUM(new_cases) as Total_cases, SUM(Cast(new_deaths as int)) as Total_Deaths, SUM(CAST(new_deaths as int))/SUM(new_cases)*100 as Death_Percentage 
from PortfolioProject..CovidDeaths
--Where location = 'India'
where continent is not null
--Group by date
Order by 1,2

 

 --Looking at Total Population vs Vaccination

 Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(int, vac.new_vaccinations)) over (Partition by dea.location Order by dea.location,
dea.date) as RollingPeopleVaccinated
 from PortfolioProject..CovidDeaths dea
 join PortfolioProject..CovidVaccination vac
	on dea.location = vac.location
	and dea.date = dea.date
where dea.continent is not null
Order by 1,2,3



 
