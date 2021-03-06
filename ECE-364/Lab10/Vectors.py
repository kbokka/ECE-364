#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-03-21 11:30:57 -0400 (Thu, 21 Mar 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab10/Vectors.py $
#$Revision: 54523 $

import sys
import os
import math

class Vector:
    def __init__(self, elements):
        self.elements = elements

    def add(self,other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Improper dimensions")
            pass

        results=[]
        for i in range(len(self.elements)):
            results.append(self.elements[i] + other.elements[i])

        vec = Vector(results)

        return vec

    def sub(self,other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Improper dimensions")

        results=[]
        for i in range(len(self.elements)):
            results.append(self.elements[i] - other.elements[i])

        vec = Vector(results)

        return vec

    def dot(self,other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Improper dimensions")

        dot=0
        for i in range(len(self.elements)):
            dot = dot + (self.elements[i]+other.elements[i])

        
        return dot

    def scale(self,by):
        elements=[]
        for i in range(len(self.elements)):
            elements.append(self.elements[i] * by)

        sca = Vector(elements)
        return sca

    def extend(self,other):
        cat=[]
        for i in range(len(self.elements)):
            cat.append(self.elements[i])
        for i in range(len(other.elements)):
            cat.append(other.elements[i])

        con = Vector(cat)
        return con

    def length(self):
        leng = len(self.elements)

        return leng
    
    def distance(self,other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Improper dimensions")

        sq=[]
        for i in range(len(self.elements)):
            sq.append((self.elements[i] - other.elements[i]) * (self.elements[i] - other.elements[i]))
        
        sum=0 
        for t in range(len(sq)):
            sum = sum + sq[t]

        return math.sqrt(sum)

    def at(self,i):
        
        return self.elements[i]

    def __str__(self):
        N=str(len(self.elements))
        temp=""
        for i in range(len(self.elements)-1):
            temp = temp + str(self.elements[i]) + ","
        temp = temp + str(self.elements[len(self.elements)-1])

        value= "Vector[" + N + "]: (" + temp + ")"
        return value

class Vector3D(Vector):
    def __int__(self,elements):
        if 3 != len(self.elements):
            raise ValueError("Improper dimensions")

        self.elements = elements

    def add(self,other):

        results=[]
        for i in range(len(self.elements)):
            results.append(self.elements[i] + other.elements[i])

        vec = Vector3D(results)
        return vec

    def sub(self,other):
        results=[]
        for i in range(len(self.elements)):
            results.append(self.elements[i] - other.elements[i])
        
        vec = Vector3D(results)
        return vec
    
    def scale(self,by):
        elements=[]
        for i in range(len(self.elements)):
            elements[i] = self.elements[i] * by

        sca = Vector3D(elements)
        return sca

    def extend(self,other):
        raise NotImplementedError

    def __str__(self):
        N=str(len(self.elements))
        temp=""
        for i in range(len(self.elements)-1):
            temp = temp + str(self.elements[i]) + ","
        temp = temp + str(self.elements[len(self.elements)-1])

        value= "Vector3D[" + N + "]: (" + temp + ")"
        return value
