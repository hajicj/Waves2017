
import com.fasterxml.jackson.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
        "relevance",
        "word",
        "word2vec"
})
public class Keyword {

    @JsonProperty("relevance")
    private Double relevance;
    @JsonProperty("word")
    private String word;
    @JsonProperty("word2vec")
    private List<Double> word2vec = null;
    @JsonIgnore
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("relevance")
    public Double getRelevance() {
        return relevance;
    }

    @JsonProperty("relevance")
    public void setRelevance(Double relevance) {
        this.relevance = relevance;
    }

    @JsonProperty("word")
    public String getWord() {
        return word;
    }

    @JsonProperty("word")
    public void setWord(String word) {
        this.word = word;
    }

    @JsonProperty("word2vec")
    public List<Double> getWord2vec() {
        return word2vec;
    }

    @JsonProperty("word2vec")
    public void setWord2vec(List<Double> word2vec) {
        this.word2vec = word2vec;
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

