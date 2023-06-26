import yaml
import serializer


class YamlSerializer(serializer.JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)


serializer.factory.register_format('YAML', YamlSerializer)
