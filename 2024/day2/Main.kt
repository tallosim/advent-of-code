package day2

import readInput
import kotlin.math.abs

const val INPUT_FILE = "2024/day2/input.txt"

private fun checkIsSafe(row: List<Long>): Boolean {
    val pairs = row.zipWithNext()

    val directions = pairs.map { (a, b) -> a > b }
    val diffs = pairs.map { (a, b) -> abs(a - b) }.map { it in 1..3 }

    return diffs.all { it } && (directions.all { it } || directions.all { !it })
}

fun main() {
    val input = readInput(INPUT_FILE)

    // Part 1
    val valid1 = input.map(::checkIsSafe).count { it }
    println("Part 1: $valid1")

    // Part 2
    val valid2 = input.map { row ->
        if (checkIsSafe(row)) return@map true
        row.indices.map { i -> row.filterIndexed { index, _ -> index != i } }.any(::checkIsSafe)
    }.count { it }
    println("Part 2: $valid2")
}