# -*- coding: utf-8 -*-
#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (31.45%)
# Total Accepted:    80.4K
# Total Submissions: 255.7K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#

class Solution:
    def reverse(self, x):
        if x == 0:
            return x
        if x < 0:
            ss = str(-x)[::-1]
            retval =  -int(ss)
            if retval < pow(-2,31):
                return 0
            else: return retval
        else:
            ss = str(x)[::-1]
            retval = int(ss)
            if retval > pow(2,31)-1:
                return 0
            else: return retval
            
