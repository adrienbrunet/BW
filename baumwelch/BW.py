#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
data = CURRENT_PATH.replace("baumwelch", "data")
hmm_python = CURRENT_PATH.replace("baumwelch", "hmmpython")

sys.path.append(hmm_python)

import encodageHmm as encod
import apprentissage as app


class HMM_BW(object):

	def __init__(self, listObservables, count):
		self.iterationCount = count
		self.listObservables = listObservables
		self.initHmm(listObservables)

		# init the alpha and beta grids #
		self.alpha = range(len(self.listObservables))
		for index in range(len(self.alpha)):
			dictOfStates = {}
			for key in self.states:
				dictOfStates[key] = 1.0/len(self.states)
			self.alpha[index] = dictOfStates

		self.beta = range(len(self.listObservables))
		for index in range(len(self.beta)):
			dictOfStates = {}
			for key in self.states:
				dictOfStates[key] = 1.0/len(self.states)
			self.beta[index] = dictOfStates


	def initHmm(self, listObservables):
		self.states = encod.get_categories(data+"/voc_etats")

		self.Pi = {}
		for key in self.states:
			self.Pi[key] = 1.0/len(self.states)

		self.transitions = {}
		for state in self.states:
			self.transitions[state] = {}
			for secondState in self.states:
				self.transitions[state][secondState] = 1.0/len(self.states)

		self.emissions = {}
		for observable in listObservables:
			self.emissions[observable] = {}
			for state in self.states:
				self.emissions[observable][state] = 1.0/len(self.states)

		return [self.states, self.transitions, self.emissions]

	def setAlpha(self):
		# init alpha(i, 1) = Pi(i) #
		for state in self.Pi:
			self.alpha[0][state] = self.Pi[state]

		# iterate forward #
		for index in range(len(self.listObservables) - 1):
			for j in self.Pi:
				sumAlpha = 0.0
				for etat in self.states:
					sumAlpha = sumAlpha + self.alpha[index][etat]*self.emissions[self.listObservables[index]][etat]*self.transitions[etat][j]
				self.alpha[index+1][j] = sumAlpha

		

	def setBeta(self):
		# init beta(i, T) = E(i, o_t) #
		for state in self.states:
			self.beta[len(self.listObservables)-1][state] = self.emissions[self.listObservables[len(self.listObservables)-1]][state]

		# iterate backward #
		for index in range(len(self.listObservables) - 2, -1, -1):
			for j in self.states:
				sumBeta = 0.0
				for etat in self.states:
					sumBeta = sumBeta + self.beta[index+1][etat]*self.emissions[self.listObservables[index+1]][etat]*self.transitions[etat][j]
				self.beta[index][j] = sumBeta

	def setGamma(self):
		a = 1+1
		#for element in grid:
		#	do sth

	def setPi(self):
		a = 1+1
		#for element in grid:
		#	do sth

	def setT(self):
		a = 1+1
		#for element in grid:
		#	do sth

	def setE(self):
		a = 1+1
		#for element in grid:
		#	do sth

	def iterate(self):
		iterations = 0
		while iterations < self.iterationCount:
			iterations = iterations + 1
