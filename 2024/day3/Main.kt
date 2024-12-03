package day3

import java.io.File

const val INPUT_FILE = "2024/day3/input.txt"

enum class Operation { MUL, DO, DONT }

fun main() {
    val input = File(INPUT_FILE).readText()
    val multiply = { m: MatchResult -> m.groupValues[1].toInt() * m.groupValues[2].toInt() }

    // Part 1
    val part1 = Regex("mul\\((\\d{1,3}),(\\d{1,3})\\)").findAll(input).sumOf(multiply)
    println("Part 1: $part1")

    // Part 2
    val part2 = listOf(
        Regex("mul\\((\\d{1,3}),(\\d{1,3})\\)").findAll(input).map { Operation.MUL to it },
        Regex("do\\(\\)").findAll(input).map { Operation.DO to it },
        Regex("don't\\(\\)").findAll(input).map { Operation.DONT to it }
    ).flatMap { it.toList() }.sortedBy { it.second.range.first }.fold(0 to true) { (acc, enabled), (operation, match) ->
        when (operation) {
            Operation.MUL -> (if (enabled) acc + multiply(match) else acc) to enabled
            Operation.DO -> acc to true
            Operation.DONT -> acc to false
        }
    }.first
    println("Part 2: $part2")
}