"""《修改》
"""

from __future__ import annotations

from typing import List

from docx import types as t
from docx.oxml.text.xiuding import CT_Ins
from docx.shared import Parented
from docx.text.run import Run


class Ins(Parented):
    """Proxy object wrapping a `<w:hyperlink>` element.

    A Ins occurs as a child of a paragraph, at the same level as a Run. A
    hyperlink itself contains runs, which is where the visible text of the hyperlink is
    stored.
    """

    def __init__(self, ins: CT_Ins, parent: t.ProvidesStoryPart):
        super().__init__(parent)
        self._parent = parent
        self._ins = self._element = ins

    @property
    def author(self) -> str:
        """
        """
        return self._ins.wAuthor or ""

    @property
    def date(self) -> str:
        """
        """
        return self._ins.wDate or ""

    @property
    def runs(self) -> List[Run]:
        """List of |Run| instances in this hyperlink.

        Together these define the visible text of the hyperlink. The text of a hyperlink
        is typically contained in a single run will be broken into multiple runs if for
        example part of the hyperlink is bold or the text was changed after the document
        was saved.
        """
        return [Run(r, self._parent) for r in self._ins.r_lst]

    @property
    def text(self) -> str:
        """String formed by concatenating the text of each run in the hyperlink.

        Tabs and line breaks in the XML are mapped to ``\\t`` and ``\\n`` characters
        respectively. Note that rendered page-breaks can occur within a hyperlink but
        they are not reflected in this text.
        """
        return self._ins.text


