import com.fasterxml.jackson.annotation.*;

import java.util.HashMap;
import java.util.Map;

@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
        "sample",
        "similarity"
})
public class Voice {

    @JsonProperty("sample")
    private String sample;
    @JsonProperty("similarity")
    private String similarity;
    @JsonIgnore
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("sample")
    public String getSample() {
        return sample;
    }

    @JsonProperty("sample")
    public void setSample(String sample) {
        this.sample = sample;
    }

    @JsonProperty("similarity")
    public String getSimilarity() {
        return similarity;
    }

    @JsonProperty("similarity")
    public void setSimilarity(String similarity) {
        this.similarity = similarity;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperty(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

}
