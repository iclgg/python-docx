"""Custom element classes related to hyperlinks (CT_Hyperlink)."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from docx.oxml.simpletypes import ST_OnOff, ST_String, XsdString
from docx.oxml.text.run import CT_R
from docx.oxml.xmlchemy import (
    BaseOxmlElement,
    OptionalAttribute,
    ZeroOrMore,
)

if TYPE_CHECKING:
    from docx.oxml.text.pagebreak import CT_LastRenderedPageBreak


class CT_Ins(BaseOxmlElement):
    """`<w:Ins>` element, containing the inserted text ."""

    r_lst: List[CT_R]

    wId: str | None = OptionalAttribute(  # pyright: ignore[reportGeneralTypeIssues]
        "w:id", XsdString
    )
    wAuthor: str | None = OptionalAttribute(  # pyright: ignore[reportGeneralTypeIssues]
        "w:author", ST_String
    )
    wDate: str | None = OptionalAttribute(  # pyright: ignore[reportGeneralTypeIssues]
        "w:date", ST_String
    )
    # history = OptionalAttribute("w:history", ST_OnOff, default=True)

    r = ZeroOrMore("w:r")

    @property
    def lastRenderedPageBreaks(self) -> List[CT_LastRenderedPageBreak]:
        """All `w:lastRenderedPageBreak` descendants of this hyperlink."""
        return self.xpath("./w:r/w:lastRenderedPageBreak")

    @property  # pyright: ignore[reportIncompatibleVariableOverride]
    def text(self) -> str:
        """The textual content of this hyperlink.

        `CT_Hyperlink` stores the hyperlink-text as one or more `w:r` children.
        """
        return "".join(r.text for r in self.xpath("w:r"))
