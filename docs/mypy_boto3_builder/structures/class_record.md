# ClassRecord

> Auto-generated documentation for [mypy_boto3_builder.structures.class_record](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py) module.

Base class for all structures that can be rendered to a class.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ClassRecord
    - [ClassRecord](#classrecord)
        - [ClassRecord().alias_name](#classrecordalias_name)
        - [ClassRecord().get_internal_imports](#classrecordget_internal_imports)
        - [ClassRecord().get_required_import_records](#classrecordget_required_import_records)
        - [ClassRecord().get_types](#classrecordget_types)
        - [ClassRecord().render_alias](#classrecordrender_alias)

## ClassRecord

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L16)

```python
dataclass
class ClassRecord():
```

Base class for all structures that can be rendered to a class.

### ClassRecord().alias_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L28)

```python
@property
def alias_name() -> str:
```

### ClassRecord().get_internal_imports

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L61)

```python
def get_internal_imports() -> List[InternalImport]:
```

### ClassRecord().get_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L47)

```python
def get_required_import_records() -> Set[ImportRecord]:
```

### ClassRecord().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L37)

```python
def get_types() -> Set[FakeAnnotation]:
```

### ClassRecord().render_alias

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L34)

```python
def render_alias() -> str:
```
