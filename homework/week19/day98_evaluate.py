# Day 98 · 自动评测：结构、空页、要点数量、长度和来源
import json
import os

EXPECTED_PAGE_COUNT = 5
VALID_PAGE_TYPES = {"标题页", "要点页", "总结页"}


def make_result(issues, metrics):
    total_penalty = sum(issue["penalty"] for issue in issues)
    has_error = any(issue["severity"] == "error" for issue in issues)

    return {
        "passed": not has_error,
        "score": max(0, 100 - total_penalty),
        "metrics": metrics,
        "issues": issues,
    }


def evaluate_outline(outline, expected, allowed_sources=None):
    issues = []
    metrics = {
        "page_count": 0,
        "empty_pages": 0,
        "too_many_points": 0,
        "too_long_points": 0,
        "invalid_sources": 0,
    }

    def add_issue(code, page, severity, message, penalty):
        issues.append({
            "code": code,
            "page": page,
            "severity": severity,
            "message": message,
            "penalty": penalty,
        })

    if not isinstance(outline, dict):
        add_issue(
            "INVALID_STRUCTURE", None, "error",
            "大纲顶层必须是字典", 20,
        )
        return make_result(issues, metrics)

    for key in ["标题", "副标题", "页"]:
        if key not in outline:
            add_issue(
                "INVALID_STRUCTURE", None, "error",
                f"大纲缺少字段：{key}", 20,
            )

    pages = outline.get("页")
    if not isinstance(pages, list):
        add_issue(
            "INVALID_STRUCTURE", None, "error",
            "字段“页”必须是列表", 20,
        )
        return make_result(issues, metrics)

    metrics["page_count"] = len(pages)

    if len(pages) != EXPECTED_PAGE_COUNT:
        add_issue(
            "WRONG_PAGE_COUNT", None, "error",
            f"页数应为 {EXPECTED_PAGE_COUNT}，实际为 {len(pages)}",
            20,
        )

    max_points = expected.get("max_points_per_page", 4)
    max_chars = expected.get("max_chars_per_point", 80)

    for page_no, page in enumerate(pages, start=1):
        if not isinstance(page, dict):
            add_issue(
                "INVALID_STRUCTURE", page_no, "error",
                f"第 {page_no} 页必须是字典", 20,
            )
            continue

        page_type = page.get("类型")
        if page_type not in VALID_PAGE_TYPES:
            add_issue(
                "INVALID_PAGE_TYPE", page_no, "error",
                f"第 {page_no} 页类型非法：{page_type}", 20,
            )

        title = page.get("标题")
        if not isinstance(title, str) or not title.strip():
            add_issue(
                "MISSING_TITLE", page_no, "error",
                f"第 {page_no} 页标题为空", 20,
            )

        points = page.get("要点")
        if not isinstance(points, list):
            add_issue(
                "INVALID_STRUCTURE", page_no, "error",
                f"第 {page_no} 页“要点”必须是列表", 20,
            )
            continue

        if not points:
            metrics["empty_pages"] += 1
            add_issue(
                "EMPTY_PAGE", page_no, "error",
                f"第 {page_no} 页没有要点", 10,
            )

        if len(points) > max_points:
            metrics["too_many_points"] += 1
            add_issue(
                "TOO_MANY_POINTS", page_no, "warning",
                f"第 {page_no} 页有 {len(points)} 个要点，"
                f"超过上限 {max_points}",
                10,
            )

        for point_no, point in enumerate(points, start=1):
            if not isinstance(point, str) or not point.strip():
                add_issue(
                    "INVALID_STRUCTURE", page_no, "error",
                    f"第 {page_no} 页第 {point_no} 条要点不是有效文字",
                    20,
                )
                continue

            if len(point) > max_chars:
                metrics["too_long_points"] += 1
                add_issue(
                    "POINT_TOO_LONG", page_no, "warning",
                    f"第 {page_no} 页第 {point_no} 条要点有 "
                    f"{len(point)} 个字符，超过上限 {max_chars}",
                    10,
                )

        if allowed_sources is not None:
            sources = page.get("来源")

            if not isinstance(sources, list) or not sources:
                add_issue(
                    "MISSING_SOURCE", page_no, "error",
                    f"第 {page_no} 页没有来源", 20,
                )
            else:
                for source in sources:
                    if source not in allowed_sources:
                        metrics["invalid_sources"] += 1
                        add_issue(
                            "INVALID_SOURCE", page_no, "error",
                            f"第 {page_no} 页来源非法：{source}", 20,
                        )

    return make_result(issues, metrics)


def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    fixture_folder = os.path.join(folder, "fixtures")

    expected = {
        "max_points_per_page": 4,
        "max_chars_per_point": 80,
    }
    allowed_sources = {f"chunk-{i:03d}" for i in range(1, 7)}

    for file_name in ["good_outline.json", "bad_outline.json"]:
        file_path = os.path.join(fixture_folder, file_name)

        with open(file_path, "r", encoding="utf-8") as f:
            outline = json.load(f)

        report = evaluate_outline(outline, expected, allowed_sources)

        print(f"\n{file_name}")
        print(f"passed={report['passed']} score={report['score']}")
        print(f"metrics={report['metrics']}")
        print(f"issue_count={len(report['issues'])}")

        for issue in report["issues"]:
            print(f"- [{issue['code']}] {issue['message']}")


if __name__ == "__main__":
    main()
