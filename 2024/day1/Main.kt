package day1

import common.readInput
import kotlin.math.abs

const val INPUT_FILE = "2024/day1/input.txt"

fun main() {
    val (left, right) = readInput(INPUT_FILE).let { input -> input.map { it[0] } to input.map { it[1] } }

    // Part 1
    val part1 = left.sorted().zip(right.sorted()).sumOf { (a, b) -> abs(a - b) }
    println("Part 1: $part1")

    // Part 2
    val rightCounts = right.groupingBy { it }.eachCount()
    val part2 = left.sumOf { it * (rightCounts[it] ?: 0) }
    println("Part 2: $part2")
}