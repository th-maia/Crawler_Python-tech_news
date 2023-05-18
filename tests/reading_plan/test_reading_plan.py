from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import patch
import pytest

mock = [
        {
            "title": "Oratória!",
            "reading_time": 15,
        },
        {
            "title": "Orkut voltou",
            "reading_time": 4,
        },
        {
            "title": "Dungleon",
            "reading_time": 3,
        },
        {
            "title": "Liguagem Lua",
            "reading_time": 12,
        },
        {
            "title": "os 20 livros",
            "reading_time": 10,
        }
    ]


def test_reading_plan_group_news():
    with patch(
        "tech_news.analyzer.reading_plan.find_news",
        return_value=mock,
    ):

        mock1 = ReadingPlanService.group_news_for_available_time(20)
        assert mock1["readable"] == [
            {'unfilled_time': 1, 'chosen_news': [
                    ('Oratória!', 15), ('Orkut voltou', 4)
                ]},
            {'unfilled_time': 5, 'chosen_news': [
                    ('Dungleon', 3), ('Liguagem Lua', 12)
                ]},
            {'unfilled_time': 10, 'chosen_news': [('os 20 livros', 10)]}]
        assert mock1['unreadable'] == []

        mock2 = ReadingPlanService.group_news_for_available_time(14)
        assert mock2['unreadable'] == [('Oratória!', 15)]

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        return ReadingPlanService.group_news_for_available_time(0)
