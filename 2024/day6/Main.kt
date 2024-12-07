package day6

import java.io.File

const val INPUT_FILE = "2024/day6/input.txt"

enum class Direction { UP, DOWN, LEFT, RIGHT }
data class Position(val x: Int, val y: Int)
data class Guard(val x: Int, val y: Int, val direction: Direction) {
    val position get() = Position(x, y)
}

data class Environment(val map: List<List<Char>>) {
    private val width = map[0].size
    private val height = map.size

    val blocks = mutableSetOf<Position>()
    val history = mutableSetOf<Guard>()
    val visited: Set<Position> get() = history.map { it.position }.toSet()

    lateinit var start: Guard
    var guard: Guard

    init {
        for (i in 0 until height) {
            for (j in 0 until width) {
                when (map[i][j]) {
                    '#' -> blocks.add(Position(i, j))
                    '^' -> start = Guard(i, j, Direction.UP)
                    'v' -> start = Guard(i, j, Direction.DOWN)
                    '<' -> start = Guard(i, j, Direction.LEFT)
                    '>' -> start = Guard(i, j, Direction.RIGHT)
                }
            }
        }
        guard = start
    }

    override fun toString(): String = buildString {
        for (i in 0 until height) {
            for (j in 0 until width) {
                append(
                    when (Position(i, j)) {
                        guard.position -> when (guard.direction) {
                            Direction.UP -> '^'
                            Direction.DOWN -> 'v'
                            Direction.LEFT -> '<'
                            Direction.RIGHT -> '>'
                        }

                        in blocks -> '#'
                        in history.map { it.position } -> 'X'
                        else -> map[i][j]
                    }
                )
            }
            append('\n')
        }
    }

    fun isInside() = guard.x in 0 until height && guard.y in 0 until width

    fun moveForward() {
        val (x, y, direction) = guard
        history.add(guard)
        guard = when (direction) {
            Direction.UP -> Guard(x - 1, y, direction)
            Direction.DOWN -> Guard(x + 1, y, direction)
            Direction.LEFT -> Guard(x, y - 1, direction)
            Direction.RIGHT -> Guard(x, y + 1, direction)
        }
    }

    fun moveRight() {
        val (i, j, direction) = guard
        history.add(guard)
        guard = when (direction) {
            Direction.UP -> Guard(i, j + 1, Direction.RIGHT)
            Direction.DOWN -> Guard(i, j - 1, Direction.LEFT)
            Direction.LEFT -> Guard(i - 1, j, Direction.UP)
            Direction.RIGHT -> Guard(i + 1, j, Direction.DOWN)
        }
    }

    fun isBlockInFront(): Boolean {
        val (i, j, direction) = guard
        return when (direction) {
            Direction.UP -> Position(i - 1, j)
            Direction.DOWN -> Position(i + 1, j)
            Direction.LEFT -> Position(i, j - 1)
            Direction.RIGHT -> Position(i, j + 1)
        } in blocks
    }

    fun isInLoop(): Boolean = guard in history
}

fun main() {
    val map = File(INPUT_FILE).readLines().map { it.toList() }

    // Part 1 - Get out of the map, count unique positions
    val env = Environment(map)
    while (env.isInside()) {
        if (env.isBlockInFront()) env.moveRight()
        else env.moveForward()

    }
    println("Part 1: ${env.visited.size}")

    // Part 2 - Find all possible new block positions, where the guard ends up in a loop
    val startEnv = Environment(map)
    var loopCount = 0
    for (block in env.visited) {
        val newEnv = startEnv.copy()
        newEnv.blocks += block

        while (newEnv.isInside()) {
            if (newEnv.isInLoop()) {
                loopCount++
                break
            }
            if (newEnv.isBlockInFront()) newEnv.moveRight()
            else newEnv.moveForward()
        }
    }
    println("Part 2: $loopCount")
}