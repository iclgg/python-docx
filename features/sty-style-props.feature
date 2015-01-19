Feature: Get and set style properties
  In order to adjust a style to suit my needs
  As a developer using python-docx
  I need a set of read/write style properties


  Scenario Outline: Get base style
    Given a style based on <base-style>
     Then style.base_style is <value>

    Examples: Base style values
      | base-style | value            |
      | no style   | None             |
      | Normal     | styles['Normal'] |


  Scenario Outline: Set base style
    Given a style based on <base-style>
     When I assign <assigned-value> to style.base_style
     Then style.base_style is <value>

    Examples: Base style values
      | base-style | assigned-value   | value            |
      | no style   | styles['Normal'] | styles['Normal'] |
      | Normal     | styles['Base']   | styles['Base']   |
      | Base       | None             | None             |


  Scenario Outline: Get hidden value
    Given a style having hidden set <setting>
     Then style.hidden is <value>

    Examples: Style hidden values
      | setting    | value |
      | on         | True  |
      | off        | False |
      | no setting | False |


  Scenario Outline: Set hidden value
    Given a style having hidden set <setting>
     When I assign <new-value> to style.hidden
     Then style.hidden is <value>

    Examples: Style hidden values
      | setting    | new-value | value |
      | no setting | True      | True  |
      | on         | False     | False |


  Scenario: Get name
    Given a style having a known name
     Then style.name is the known name


  Scenario: Set name
    Given a style having a known name
     When I assign a new name to the style
     Then style.name is the new name


  Scenario Outline: Get style display sort order
    Given a style having priority of <setting>
     Then style.priority is <value>

    Examples: style.priority values
      | setting    | value |
      | no setting | None  |
      | 42         | 42    |


  Scenario Outline: Set style display sort order
    Given a style having priority of <setting>
     When I assign <new-value> to style.priority
     Then style.priority is <value>

    Examples: Style priority values
      | setting    | new-value | value |
      | no setting | 42        | 42    |
      | 42         | 24        | 24    |
      | 42         | None      | None  |


  Scenario: Get style id
    Given a style having a known style id
     Then style.style_id is the known style id


  Scenario: Set style id
    Given a style having a known style id
     When I assign a new value to style.style_id
     Then style.style_id is the new style id


  Scenario: Get style type
    Given a style having a known type
     Then style.type is the known type


  @wip
  Scenario Outline: Get unhide-when-used value
    Given a style having unhide-when-used set <setting>
     Then style.unhide_when_used is <value>

    Examples: Style unhide-when-used values
      | setting    | value |
      | on         | True  |
      | off        | False |
      | no setting | False |


  @wip
  Scenario Outline: Set unhide-when-used value
    Given a style having unhide-when-used set <setting>
     When I assign <new-value> to style.unhide_when_used
     Then style.unhide_when_used is <value>

    Examples: Style unhide_when_used values
      | setting    | new-value | value |
      | no setting | True      | True  |
      | on         | False     | False |
