package day7

import readInput
import kotlin.math.pow

const val INPUT_FILE = "2024/day7/input.txt"

enum class Operator { ADD, MULTIPLY, COMBINE }

fun Int.pow(exponent: Int) = toDouble().pow(exponent).toInt()

fun getCombinations(n: Int, operators: Set<Operator>) = (0 until operators.size.pow(n)).map { i ->
    var current = i
    (0 until n).map { _ ->
        val mod = current % operators.size
        current /= operators.size
        operators.toList()[mod]
    }
}

fun solve(equations: List<Pair<Long, List<Long>>>, operators: Set<Operator>) = equations.sumOf { (result, numbers) ->
    getCombinations(numbers.size - 1, operators).firstOrNull { combination ->
        result == numbers.subList(1, numbers.size).foldIndexed(numbers[0]) { i, acc, number ->
            when (combination[i]) {
                Operator.ADD -> acc + number
                Operator.MULTIPLY -> acc * number
                Operator.COMBINE -> "$acc$number".toLong()
            }
        }
    }?.let { result } ?: 0L
}

fun main() {
    val input = readInput(INPUT_FILE)
    val equations = input.map { it[0] to it.drop(1) }

    val part1 = solve(equations, setOf(Operator.ADD, Operator.MULTIPLY))
    val part2 = solve(equations, setOf(Operator.ADD, Operator.MULTIPLY, Operator.COMBINE))

    println("Part 1: $part1")
    println("Part 2: $part2")
}